import yt_dlp
from pytubefix import YouTube
from colorama import Fore, Style, init
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import validate_url

# Inicializar colorama para Windows
init()

class VideoInfo:
    def __init__(self):
        pass

    def get_video_info(self, url):
        """Obtiene información del video usando pytubefix (método principal)"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return None

        try:
            print(f"{Fore.CYAN}🔄 Obteniendo información del video...{Style.RESET_ALL}")
            
            # Usar pytubefix con mejor configuración
            yt = YouTube(url, use_oauth=False, allow_oauth_cache=True, client='WEB')
            
            # Formatear duración
            duration_str = f"{yt.length // 60}:{yt.length % 60:02d}" if yt.length else "Desconocido"
            
            # Obtener calidades disponibles (tanto progresivos como adaptativos)
            progressive_streams = yt.streams.filter(progressive=True, file_extension='mp4')
            adaptive_streams = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4')
            
            # Combinar calidades de ambos tipos de streams
            qualities = set()
            for stream in progressive_streams:
                if stream.resolution:
                    qualities.add(int(stream.resolution.replace('p', '')))
            
            for stream in adaptive_streams:
                if stream.resolution:
                    qualities.add(int(stream.resolution.replace('p', '')))
            
            qualities = sorted(list(qualities), reverse=True)
            
            # Mostrar información usando pytubefix
            self._display_video_info_pytubefix(yt, duration_str, qualities)
            
            return {
                'title': yt.title,
                'uploader': yt.author,
                'duration': duration_str,
                'view_count': yt.views,
                'upload_date': yt.publish_date.strftime('%Y%m%d') if yt.publish_date else 'N/A',
                'description': yt.description,
                'qualities': qualities,
                'channel_url': yt.channel_url,
                'thumbnail_url': yt.thumbnail_url
            }

        except Exception as e:
            print(f"{Fore.RED}❌ Error obteniendo información con pytubefix: {str(e)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}🔄 Intentando con yt-dlp como respaldo...{Style.RESET_ALL}")
            return self.get_video_info_ytdlp(url)

    def get_video_info_ytdlp(self, url):
        """Obtiene información del video usando yt-dlp (método de respaldo)"""
        try:
            print(f"{Fore.CYAN}🔄 Obteniendo información del video con yt-dlp...{Style.RESET_ALL}")
            
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Formatear duración
                duration = info.get('duration', 0)
                duration_str = f"{duration // 60}:{duration % 60:02d}" if duration else "Desconocido"
                
                # Obtener formatos disponibles
                formats = info.get('formats', [])
                qualities = set()
                for fmt in formats:
                    if fmt.get('height'):
                        qualities.add(fmt['height'])
                
                qualities = sorted(list(qualities), reverse=True)
                
                # Mostrar información usando yt-dlp
                self._display_video_info_ytdlp(info, duration_str, qualities)
                
                return {
                    'title': info.get('title', 'N/A'),
                    'uploader': info.get('uploader', 'N/A'),
                    'duration': duration_str,
                    'view_count': info.get('view_count', 0),
                    'upload_date': info.get('upload_date', 'N/A'),
                    'description': info.get('description', ''),
                    'qualities': qualities,
                    'channel_url': info.get('channel_url', 'N/A'),
                    'thumbnail_url': info.get('thumbnail', 'N/A')
                }

        except Exception as e:
            print(f"{Fore.RED}❌ Error obteniendo información con yt-dlp: {str(e)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 No se pudo obtener información del video{Style.RESET_ALL}")
            return None

    def _display_video_info_pytubefix(self, yt, duration_str, qualities):
        """Muestra la información del video usando datos de pytubefix"""
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"📋 INFORMACIÓN DEL VIDEO (PyTubeFix)")
        print(f"{'='*60}{Style.RESET_ALL}")
        
        print(f"{Fore.YELLOW}📹 Título: {Style.RESET_ALL}{yt.title}")
        print(f"{Fore.YELLOW}👤 Autor: {Style.RESET_ALL}{yt.author}")
        print(f"{Fore.YELLOW}📺 Canal: {Style.RESET_ALL}{yt.channel_url}")
        print(f"{Fore.YELLOW}⏱️ Duración: {Style.RESET_ALL}{duration_str}")
        print(f"{Fore.YELLOW}👁️ Vistas: {Style.RESET_ALL}{yt.views:,}")
        
        if yt.publish_date:
            formatted_date = yt.publish_date.strftime('%d/%m/%Y')
            print(f"{Fore.YELLOW}📅 Fecha de publicación: {Style.RESET_ALL}{formatted_date}")
        
        if qualities:
            qualities_str = ', '.join([f"{q}p" for q in qualities])
            print(f"{Fore.YELLOW}🎥 Calidades disponibles: {Style.RESET_ALL}{qualities_str}")
        
        # Mostrar información adicional de streams
        print(f"\n{Fore.CYAN}📊 Información de streams disponibles:{Style.RESET_ALL}")
        
        # Streams progresivos
        progressive_streams = yt.streams.filter(progressive=True, file_extension='mp4')
        if progressive_streams:
            print(f"{Fore.GREEN}  🎬 Videos progresivos (video + audio):{Style.RESET_ALL}")
            for stream in progressive_streams:
                size_mb = stream.filesize_mb if hasattr(stream, 'filesize_mb') else 'N/A'
                print(f"    • {stream.resolution} - {size_mb} MB")
        
        # Streams adaptativos de video
        adaptive_video = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4')
        if adaptive_video:
            print(f"{Fore.GREEN}  🎥 Videos adaptativos (solo video):{Style.RESET_ALL}")
            for stream in list(adaptive_video)[:5]:  # Mostrar solo los primeros 5
                size_mb = stream.filesize_mb if hasattr(stream, 'filesize_mb') else 'N/A'
                print(f"    • {stream.resolution} - {size_mb} MB")
        
        # Streams de audio
        audio_streams = yt.streams.filter(only_audio=True)
        if audio_streams:
            print(f"{Fore.GREEN}  🎵 Audio disponible:{Style.RESET_ALL}")
            for stream in list(audio_streams)[:3]:  # Mostrar solo los primeros 3
                size_mb = stream.filesize_mb if hasattr(stream, 'filesize_mb') else 'N/A'
                print(f"    • {stream.mime_type} - {size_mb} MB")
        
        # Descripción 
        if yt.description:
            print(f"\n{Fore.YELLOW}📝 Descripción:{Style.RESET_ALL}")
            
            # Mostrar hasta 500 caracteres en lugar de 150
            if len(yt.description) > 500:
                desc_preview = yt.description[:500] + '...'
                print(f"  {desc_preview}")
                
                # Opción para mostrar descripción completa
                show_full = input(f"\n{Fore.CYAN}¿Mostrar descripción completa? (s/n): {Style.RESET_ALL}").strip().lower()
                if show_full in ['s', 'si', 'sí', 'y', 'yes']:
                    print(f"\n{Fore.YELLOW}📝 Descripción completa:{Style.RESET_ALL}")
                    
                    # Dividir la descripción en líneas de máximo 80 caracteres para mejor legibilidad
                    desc_lines = self._format_description(yt.description)
                    for line in desc_lines:
                        print(f"  {line}")
            else:
                print(f"  {yt.description}")
        
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}")

    def _display_video_info_ytdlp(self, info, duration_str, qualities):
        """Muestra la información del video usando datos de yt-dlp"""
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"📋 INFORMACIÓN DEL VIDEO (yt-dlp)")
        print(f"{'='*60}{Style.RESET_ALL}")
        
        print(f"{Fore.YELLOW}📹 Título: {Style.RESET_ALL}{info.get('title', 'N/A')}")
        print(f"{Fore.YELLOW}👤 Autor: {Style.RESET_ALL}{info.get('uploader', 'N/A')}")
        print(f"{Fore.YELLOW}⏱️ Duración: {Style.RESET_ALL}{duration_str}")
        
        view_count = info.get('view_count')
        if view_count:
            print(f"{Fore.YELLOW}👁️ Vistas: {Style.RESET_ALL}{view_count:,}")
        
        upload_date = info.get('upload_date')
        if upload_date and len(upload_date) == 8:
            formatted_date = f"{upload_date[6:8]}/{upload_date[4:6]}/{upload_date[:4]}"
            print(f"{Fore.YELLOW}📅 Fecha de subida: {Style.RESET_ALL}{formatted_date}")
        
        if qualities:
            qualities_str = ', '.join([f"{q}p" for q in qualities])
            print(f"{Fore.YELLOW}🎥 Calidades disponibles: {Style.RESET_ALL}{qualities_str}")
        
        # Descripción 
        description = info.get('description', '')
        if description:
            print(f"\n{Fore.YELLOW}📝 Descripción:{Style.RESET_ALL}")
            
            # Mostrar hasta 500 caracteres en lugar de 150
            if len(description) > 500:
                desc_preview = description[:500] + '...'
                print(f"  {desc_preview}")
                
                # Opción para mostrar descripción completa
                show_full = input(f"\n{Fore.CYAN}¿Mostrar descripción completa? (s/n): {Style.RESET_ALL}").strip().lower()
                if show_full in ['s', 'si', 'sí', 'y', 'yes']:
                    print(f"\n{Fore.YELLOW}📝 Descripción completa:{Style.RESET_ALL}")
                    
                    # Dividir la descripción en líneas para mejor legibilidad
                    desc_lines = self._format_description(description)
                    for line in desc_lines:
                        print(f"  {line}")
            else:
                print(f"  {description}")
        
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}")

    def _format_description(self, description):
        """Formatea la descripción para mejor legibilidad"""
        # Dividir por saltos de línea existentes
        lines = description.split('\n')
        formatted_lines = []
        
        for line in lines:
            # Si la línea es muy larga, dividirla en chunks de 80 caracteres
            if len(line) > 80:
                words = line.split(' ')
                current_line = ""
                
                for word in words:
                    if len(current_line + word + " ") <= 80:
                        current_line += word + " "
                    else:
                        if current_line:
                            formatted_lines.append(current_line.strip())
                        current_line = word + " "
                
                if current_line:
                    formatted_lines.append(current_line.strip())
            else:
                formatted_lines.append(line)
        
        return formatted_lines

    def show_available_qualities(self):
        """Muestra las calidades disponibles para descarga"""
        qualities = ['best', '1080p', '720p', '480p', '360p', '240p', 'worst']
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"🎥 CALIDADES DISPONIBLES PARA DESCARGA")
        print(f"{'='*50}{Style.RESET_ALL}")
        
        print(f"{Fore.GREEN}📱 Métodos de descarga:{Style.RESET_ALL}")
        print(f"  1️⃣ yt-dlp (Recomendado) - Más estable y versátil")
        print(f"  2️⃣ pytubefix - Más rápido para obtener información")
        
        print(f"\n{Fore.YELLOW}🎬 Calidades disponibles:{Style.RESET_ALL}")
        for i, quality in enumerate(qualities, 1):
            emoji = "🏆" if quality == "best" else "📺" if quality in ["1080p", "720p"] else "📱" if quality in ["480p", "360p"] else "⚡" if quality == "worst" else "📝"
            print(f"  {emoji} {quality}")
        
        print(f"\n{Fore.CYAN}💡 Consejos:{Style.RESET_ALL}")
        print(f"  • 'best' descarga la mejor calidad disponible")
        print(f"  • '1080p' y '720p' son ideales para pantallas grandes")
        print(f"  • '480p' y '360p' son perfectas para móviles")
        print(f"  • 'worst' descarga la menor calidad (menor tamaño)")
        
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}")

    def get_detailed_stream_info(self, url):
        """Obtiene información detallada de todos los streams disponibles"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return None

        try:
            print(f"{Fore.CYAN}🔄 Analizando streams disponibles...{Style.RESET_ALL}")
            yt = YouTube(url, use_oauth=False, allow_oauth_cache=True, client='WEB')
            
            print(f"\n{Fore.GREEN}📊 ANÁLISIS DETALLADO DE STREAMS{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📹 Video: {yt.title}{Style.RESET_ALL}")
            
            # Todos los streams disponibles
            all_streams = yt.streams
            
            print(f"\n{Fore.CYAN}📋 Todos los streams disponibles:{Style.RESET_ALL}")
            for i, stream in enumerate(all_streams, 1):
                size_mb = stream.filesize_mb if hasattr(stream, 'filesize_mb') else 'N/A'
                print(f"  {i:2d}. {stream}")
                print(f"      📁 Tamaño: {size_mb} MB")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
            return False