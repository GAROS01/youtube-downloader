import os
import yt_dlp
from pytubefix import YouTube
from colorama import Fore, Style, init
from tqdm import tqdm
import sys
import threading
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import validate_url, format_filename

# Inicializar colorama para Windows
init()

class Downloader:
    def __init__(self, download_path="downloads"):
        self.download_path = download_path
        self.create_download_directory()
        self.progress_bar = None

    def create_download_directory(self):
        """Crea el directorio de descarga si no existe"""
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def progress_hook(self, d):
        """Hook de progreso para yt-dlp"""
        if d['status'] == 'downloading':
            if self.progress_bar is None:
                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                if total_bytes > 0:
                    self.progress_bar = tqdm(
                        total=total_bytes,
                        unit='B',
                        unit_scale=True,
                        desc=f"{Fore.CYAN}📥 Descargando{Style.RESET_ALL}",
                        bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{rate_fmt}]'
                    )
            
            if self.progress_bar:
                downloaded_bytes = d.get('downloaded_bytes', 0)
                self.progress_bar.n = downloaded_bytes
                self.progress_bar.refresh()
                
        elif d['status'] == 'finished':
            if self.progress_bar:
                self.progress_bar.close()
                self.progress_bar = None
            print(f"\n{Fore.GREEN}✅ Descarga completada: {os.path.basename(d['filename'])}{Style.RESET_ALL}")

    def download_video(self, url, quality='best', audio_only=False):
        """Descarga video usando yt-dlp con configuración mejorada para máxima calidad"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return False

        try:
            # Configuración mejorada de yt-dlp para máxima calidad
            format_selector = self._get_format_selector_improved(quality, audio_only)
            
            ydl_opts = {
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'format': format_selector,
                'progress_hooks': [self.progress_hook],
                'merge_output_format': 'mp4',  # Fusionar en MP4
                'writesubtitles': False,
                'writeautomaticsub': False,
                'ignoreerrors': False,
            }

            if audio_only:
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',  # Máxima calidad de audio MP3
                    }]
                })
                print(f"{Fore.CYAN}🎵 Descargando audio en máxima calidad (320kbps MP3)...{Style.RESET_ALL}")
            else:
                print(f"{Fore.CYAN}🎬 Descargando video en calidad: {quality}...{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}📊 Formato: {format_selector}{Style.RESET_ALL}")
                
                # Verificar si FFmpeg está disponible para fusión
                if not self._check_ffmpeg():
                    print(f"{Fore.YELLOW}⚠️ FFmpeg no detectado. Puede que no se pueda combinar video+audio en máxima calidad{Style.RESET_ALL}")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Obtener información del video primero
                info = ydl.extract_info(url, download=False)
                print(f"{Fore.GREEN}📹 Título: {info.get('title', 'N/A')}{Style.RESET_ALL}")
                
                # Mostrar formato seleccionado
                if not audio_only:
                    self._show_selected_formats(ydl, url, format_selector)
                
                # Descargar
                ydl.download([url])
            
            print(f"{Fore.GREEN}🎉 Descarga completada exitosamente{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📁 Guardado en: {self.download_path}{Style.RESET_ALL}")
            return True

        except Exception as e:
            if self.progress_bar:
                self.progress_bar.close()
                self.progress_bar = None
            print(f"{Fore.RED}❌ Error durante la descarga: {str(e)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 Sugerencias:{Style.RESET_ALL}")
            print(f"   • Verifica que la URL sea válida y el video esté disponible")
            print(f"   • Intenta con una calidad menor si hay problemas")
            print(f"   • Asegúrate de tener FFmpeg instalado para máxima calidad")
            return False

    def _get_format_selector_improved(self, quality, audio_only):
        """Devuelve el selector de formato mejorado para obtener máxima calidad"""
        if audio_only:
            return 'bestaudio[acodec^=mp4a]/bestaudio[acodec^=mp3]/bestaudio/best'
        
        # Configuraciones mejoradas que combinan video + audio para máxima calidad
        quality_map = {
            'best': 'bestvideo[height<=?1080]+bestaudio/best[height<=?1080]',
            '2160p': 'bestvideo[height<=?2160]+bestaudio/best[height<=?2160]',  # 4K
            '1440p': 'bestvideo[height<=?1440]+bestaudio/best[height<=?1440]',  # 2K
            '1080p': 'bestvideo[height<=?1080][height>720]+bestaudio/bestvideo[height<=?1080]+bestaudio/best[height<=?1080]',
            '720p': 'bestvideo[height<=?720][height>480]+bestaudio/bestvideo[height<=?720]+bestaudio/best[height<=?720]',
            '480p': 'bestvideo[height<=?480][height>360]+bestaudio/bestvideo[height<=?480]+bestaudio/best[height<=?480]',
            '360p': 'bestvideo[height<=?360][height>240]+bestaudio/bestvideo[height<=?360]+bestaudio/best[height<=?360]',
            '240p': 'bestvideo[height<=?240]+bestaudio/best[height<=?240]',
            'worst': 'worstvideo+bestaudio/worst'
        }
        
        return quality_map.get(quality, quality_map['best'])

    def _show_selected_formats(self, ydl, url, format_selector):
        """Muestra los formatos que serán descargados"""
        try:
            print(f"{Fore.CYAN}🔍 Analizando formatos disponibles...{Style.RESET_ALL}")
            
            # Obtener información detallada de formatos
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            
            # Simular la selección de formato que hará yt-dlp
            print(f"{Fore.GREEN}📊 Formatos que se descargarán:{Style.RESET_ALL}")
            
            # Mostrar algunos de los mejores formatos disponibles
            video_formats = [f for f in formats if f.get('vcodec', 'none') != 'none' and f.get('height')]
            audio_formats = [f for f in formats if f.get('acodec', 'none') != 'none' and not f.get('height')]
            
            if video_formats:
                best_video = max(video_formats, key=lambda x: (x.get('height', 0), x.get('fps', 0)))
                print(f"  🎥 Video: {best_video.get('height', 'N/A')}p @ {best_video.get('fps', 'N/A')}fps ({best_video.get('vcodec', 'N/A')})")
                
            if audio_formats:
                best_audio = max(audio_formats, key=lambda x: x.get('abr', 0) or 0)
                print(f"  🎵 Audio: {best_audio.get('abr', 'N/A')}kbps ({best_audio.get('acodec', 'N/A')})")
                
        except Exception as e:
            print(f"{Fore.YELLOW}⚠️ No se pudo mostrar información de formatos: {str(e)}{Style.RESET_ALL}")

    def _check_ffmpeg(self):
        """Verifica si FFmpeg está disponible"""
        try:
            import subprocess
            result = subprocess.run(['ffmpeg', '-version'], 
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except:
            return False

    def progress_function_pytube(self, stream, chunk, bytes_remaining):
        """Función de progreso para pytubefix"""
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        
        if hasattr(self, '_pytube_pbar'):
            self._pytube_pbar.update(len(chunk))
        else:
            self._pytube_pbar = tqdm(
                total=total_size,
                unit='B',
                unit_scale=True,
                desc=f"{Fore.CYAN}📥 Descargando{Style.RESET_ALL}",
                bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{rate_fmt}]'
            )
            self._pytube_pbar.update(bytes_downloaded)

    def download_video_pytube(self, url, quality='highest'):
        """Descarga video usando pytubefix con barra de progreso"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return False

        try:
            print(f"{Fore.CYAN}🔄 Obteniendo información del video con pytubefix...{Style.RESET_ALL}")
            
            # Crear objeto YouTube con mejor configuración
            yt = YouTube(url, use_oauth=False, allow_oauth_cache=True, client='WEB')
            
            # Registrar el callback de progreso
            yt.register_on_progress_callback(self.progress_function_pytube)
            
            # Seleccionar stream con más opciones de calidad
            stream = self._select_pytube_stream(yt, quality)
            
            if not stream:
                print(f"{Fore.YELLOW}⚠️ Calidad {quality} no disponible{Style.RESET_ALL}")
                # Mostrar calidades disponibles
                available = [s.resolution for s in yt.streams.filter(progressive=True) if s.resolution]
                if available:
                    print(f"{Fore.CYAN}🎥 Calidades disponibles: {', '.join(set(available))}{Style.RESET_ALL}")
                stream = yt.streams.get_highest_resolution()

            print(f"\n{Fore.GREEN}📋 Información de la descarga:{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📹 Título: {yt.title[:50]}{'...' if len(yt.title) > 50 else ''}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}🎥 Calidad: {stream.resolution or 'Audio only'}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📊 Tamaño: {stream.filesize_mb:.1f} MB{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📁 Formato: {stream.mime_type}{Style.RESET_ALL}")
            
            # Advertir si no es la máxima calidad
            if stream.resolution and quality in ['1080p', 'highest']:
                available_resolutions = [s.resolution for s in yt.streams.filter(progressive=True) if s.resolution]
                max_available = max([int(r.replace('p', '')) for r in available_resolutions] or [0])
                current_res = int(stream.resolution.replace('p', ''))
                
                if current_res < max_available:
                    print(f"{Fore.YELLOW}⚠️ Nota: Usando stream progresivo. Para máxima calidad usa yt-dlp (opción 1){Style.RESET_ALL}")
            
            # Inicializar variables para la barra de progreso
            self._pytube_pbar = None
            
            print(f"\n{Fore.CYAN}🚀 Iniciando descarga...{Style.RESET_ALL}")

            # Descargar
            stream.download(output_path=self.download_path)
            
            # Cerrar barra de progreso si existe
            if hasattr(self, '_pytube_pbar') and self._pytube_pbar:
                self._pytube_pbar.close()
                delattr(self, '_pytube_pbar')
            
            print(f"\n{Fore.GREEN}🎉 Descarga completada exitosamente{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📁 Guardado en: {self.download_path}{Style.RESET_ALL}")
            return True

        except Exception as e:
            # Cerrar barra de progreso en caso de error
            if hasattr(self, '_pytube_pbar') and self._pytube_pbar:
                self._pytube_pbar.close()
                delattr(self, '_pytube_pbar')
            print(f"{Fore.RED}❌ Error durante la descarga: {str(e)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 Intenta con la opción de yt-dlp (opción 1) para mejor calidad{Style.RESET_ALL}")
            return False

    def _select_pytube_stream(self, yt, quality):
        """Selecciona el stream apropiado basado en la calidad especificada"""
        try:
            if quality == 'highest':
                return yt.streams.get_highest_resolution()
            elif quality == 'lowest':
                return yt.streams.get_lowest_resolution()
            elif quality in ['1080p', '720p', '480p', '360p', '240p']:
                # Primero intentar con streams progresivos
                stream = yt.streams.filter(res=quality, progressive=True).first()
                if not stream:
                    # Si no hay progresivo, intentar con adaptativo
                    stream = yt.streams.filter(res=quality, adaptive=True).first()
                return stream
            else:
                return yt.streams.get_highest_resolution()
        except Exception as e:
            print(f"{Fore.YELLOW}⚠️ Error seleccionando calidad específica: {e}{Style.RESET_ALL}")
            return yt.streams.get_highest_resolution()

    def download_best_quality_separate(self, url):
        """Descarga video y audio por separado y los combina (máxima calidad)"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return False

        print(f"{Fore.CYAN}🎯 Descarga en máxima calidad (video + audio separados){Style.RESET_ALL}")
        
        # Configuración específica para máxima calidad
        ydl_opts = {
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',  # Mejor video + mejor audio
            'merge_output_format': 'mp4',
            'progress_hooks': [self.progress_hook],
            'writesubtitles': False,
            'writeautomaticsub': False,
        }
        
        return self._download_with_config(url, ydl_opts)

    def _download_with_config(self, url, ydl_opts):
        """Descarga con configuración específica"""
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            print(f"{Fore.GREEN}🎉 Descarga completada exitosamente{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📁 Guardado en: {self.download_path}{Style.RESET_ALL}")
            return True
        except Exception as e:
            if self.progress_bar:
                self.progress_bar.close()
                self.progress_bar = None
            print(f"{Fore.RED}❌ Error durante la descarga: {str(e)}{Style.RESET_ALL}")
            return False

    def show_available_qualities(self):
        """Muestra las calidades disponibles con explicaciones mejoradas"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"🎥 CALIDADES Y MÉTODOS DE DESCARGA DISPONIBLES")
        print(f"{'='*60}{Style.RESET_ALL}")
        
        print(f"{Fore.GREEN}📱 Métodos de descarga:{Style.RESET_ALL}")
        print(f"  1️⃣ yt-dlp (🏆 RECOMENDADO) - Combina mejor video + mejor audio")
        print(f"  2️⃣ pytubefix - Streams progresivos (limitado pero rápido)")
        
        print(f"\n{Fore.YELLOW}🎬 Calidades disponibles para yt-dlp:{Style.RESET_ALL}")
        qualities = [
            ('best', '🏆', 'Máxima calidad disponible (hasta 4K si está disponible)'),
            ('2160p', '🎬', '4K Ultra HD (si está disponible)'),
            ('1440p', '📺', '2K Quad HD (si está disponible)'),
            ('1080p', '🎥', 'Full HD - Combina video 1080p + mejor audio'),
            ('720p', '📱', 'HD - Perfecto para móviles y tablets'),
            ('480p', '💻', 'SD - Buena calidad, menor tamaño'),
            ('360p', '📞', 'Baja calidad - Para conexiones lentas'),
            ('240p', '⚡', 'Mínima calidad - Máximo ahorro de datos'),
            ('worst', '💾', 'Peor calidad disponible - Menor tamaño de archivo')
        ]
        
        for quality, emoji, desc in qualities:
            print(f"  {emoji} {quality:<8} - {desc}")
        
        print(f"\n{Fore.CYAN}🔧 Características de yt-dlp:{Style.RESET_ALL}")
        print(f"  ✅ Combina automáticamente video de alta calidad + audio de alta calidad")
        print(f"  ✅ Soporta formatos hasta 4K y audio hasta 320kbps")
        print(f"  ✅ Usa FFmpeg para fusionar streams (se instala automáticamente)")
        print(f"  ✅ Mejor compatibilidad con diferentes tipos de videos")
        
        print(f"\n{Fore.YELLOW}📊 Características de pytubefix:{Style.RESET_ALL}")
        print(f"  ⚠️ Solo streams progresivos (video+audio en un solo archivo)")
        print(f"  ⚠️ Limitado a calidades que YouTube ofrece como progresivos")
        print(f"  ✅ Más rápido para obtener información del video")
        print(f"  ✅ No requiere FFmpeg")
        
        print(f"\n{Fore.GREEN}💡 Recomendaciones:{Style.RESET_ALL}")
        print(f"  🎯 Para máxima calidad: Usa yt-dlp con 'best' o '1080p'")
        print(f"  📱 Para dispositivos móviles: '720p' o '480p'")
        print(f"  💾 Para ahorrar espacio: '360p' o 'worst'")
        print(f"  🎵 Para solo audio: Usar opción 3 (MP3 a 320kbps)")
        
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")

    def get_video_info(self, url):
        """Obtiene información del video con barra de progreso"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return None

        try:
            # Simular progreso para obtener información
            with tqdm(total=100, desc=f"{Fore.CYAN}📊 Obteniendo info{Style.RESET_ALL}", 
                     bar_format='{l_bar}{bar}| {percentage:3.0f}%') as pbar:
                
                pbar.update(30)
                yt = YouTube(url)
                pbar.update(40)
                
                info = {
                    'title': yt.title,
                    'author': yt.author,
                    'length': yt.length,
                    'views': yt.views,
                    'description': yt.description[:200] + '...' if len(yt.description) > 200 else yt.description,
                    'thumbnail_url': yt.thumbnail_url,
                    'available_qualities': [stream.resolution for stream in yt.streams.filter(progressive=True, file_extension='mp4')]
                }
                pbar.update(30)
            
            print(f"\n{Fore.GREEN}📋 Información del video:{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📹 Título: {info['title']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}👤 Autor: {info['author']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}⏱️ Duración: {info['length']} segundos{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}👁️ Vistas: {info['views']:,}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}🎥 Calidades disponibles: {', '.join(filter(None, info['available_qualities']))}{Style.RESET_ALL}")
            
            return info

        except Exception as e:
            print(f"{Fore.RED}❌ Error obteniendo información: {str(e)}{Style.RESET_ALL}")
            return None

    def download_multiple_videos(self, urls, quality='best'):
        """Descarga múltiples videos con barra de progreso general"""
        if not urls:
            print(f"{Fore.RED}❌ No se proporcionaron URLs{Style.RESET_ALL}")
            return False

        print(f"{Fore.CYAN}📦 Descargando {len(urls)} videos en calidad: {quality}...{Style.RESET_ALL}")
        
        success_count = 0
        with tqdm(total=len(urls), desc=f"{Fore.GREEN}🎬 Videos{Style.RESET_ALL}", 
                 unit="video", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} videos') as main_pbar:
            
            for i, url in enumerate(urls, 1):
                print(f"\n{Fore.YELLOW}📹 Descargando video {i}/{len(urls)}{Style.RESET_ALL}")
                if self.download_video(url, quality):
                    success_count += 1
                main_pbar.update(1)
        
        print(f"\n{Fore.GREEN}🎉 Descarga completada: {success_count}/{len(urls)} videos exitosos{Style.RESET_ALL}")
        return success_count == len(urls)