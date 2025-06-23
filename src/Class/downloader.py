import os
import yt_dlp
from pytubefix import YouTube
from colorama import Fore, Style, init
from tqdm import tqdm
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import validate_url, format_filename

# Inicializar colorama para Windows
init()

class Downloader:
    def __init__(self, download_path="downloads"):
        self.download_path = download_path
        self.create_download_directory()

    def create_download_directory(self):
        """Crea el directorio de descarga si no existe"""
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def download_video(self, url, quality='best', audio_only=False):
        """Descarga video usando yt-dlp"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return False

        try:
            # Configuración de yt-dlp con mejores opciones de calidad
            format_selector = self._get_format_selector(quality, audio_only)
            
            ydl_opts = {
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'format': format_selector,
            }

            if audio_only:
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            print(f"{Fore.CYAN}🔄 Descargando video en calidad: {quality}...{Style.RESET_ALL}")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            print(f"{Fore.GREEN}✅ Descarga completada exitosamente{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📁 Guardado en: {self.download_path}{Style.RESET_ALL}")
            return True

        except Exception as e:
            print(f"{Fore.RED}❌ Error durante la descarga: {str(e)}{Style.RESET_ALL}")
            return False

    def download_video_pytube(self, url, quality='highest'):
        """Descarga video usando pytubefix (alternativo actualizado)"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return False

        try:
            print(f"{Fore.CYAN}🔄 Obteniendo información del video con pytubefix...{Style.RESET_ALL}")
            
            # Crear objeto YouTube con mejor configuración
            yt = YouTube(url, use_oauth=False, allow_oauth_cache=True, client='WEB')
            
            # Seleccionar stream con más opciones de calidad
            stream = self._select_pytube_stream(yt, quality)
            
            if not stream:
                print(f"{Fore.YELLOW}⚠️ Calidad {quality} no disponible, usando la mejor disponible{Style.RESET_ALL}")
                stream = yt.streams.get_highest_resolution()

            print(f"{Fore.YELLOW}📹 Título: {yt.title}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}🎥 Calidad: {stream.resolution or 'Audio only'}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📊 Tamaño: {stream.filesize_mb:.1f} MB{Style.RESET_ALL}")
            print(f"{Fore.CYAN}🔄 Descargando...{Style.RESET_ALL}")

            # Descargar
            stream.download(output_path=self.download_path)
            
            print(f"{Fore.GREEN}✅ Descarga completada exitosamente{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📁 Guardado en: {self.download_path}{Style.RESET_ALL}")
            return True

        except Exception as e:
            print(f"{Fore.RED}❌ Error durante la descarga: {str(e)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 Intenta con la opción de yt-dlp (opción 1){Style.RESET_ALL}")
            return False

    def _get_format_selector(self, quality, audio_only):
        """Devuelve el selector de formato apropiado para yt-dlp"""
        if audio_only:
            return 'bestaudio/best'
        
        quality_map = {
            'best': 'best[height<=1080]',
            '1080p': 'best[height<=1080]',
            '720p': 'best[height<=720]',
            '480p': 'best[height<=480]',
            '360p': 'best[height<=360]',
            '240p': 'best[height<=240]',
            'worst': 'worst'
        }
        
        return quality_map.get(quality, 'best[height<=1080]')

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

    def get_video_info(self, url):
        """Obtiene información del video"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return None

        try:
            yt = YouTube(url)
            info = {
                'title': yt.title,
                'author': yt.author,
                'length': yt.length,
                'views': yt.views,
                'description': yt.description[:200] + '...' if len(yt.description) > 200 else yt.description,
                'thumbnail_url': yt.thumbnail_url,
                'available_qualities': [stream.resolution for stream in yt.streams.filter(progressive=True, file_extension='mp4')]
            }
            
            print(f"{Fore.GREEN}📋 Información del video:{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📹 Título: {info['title']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}👤 Autor: {info['author']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}⏱️ Duración: {info['length']} segundos{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}👁️ Vistas: {info['views']:,}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}🎥 Calidades disponibles: {', '.join(filter(None, info['available_qualities']))}{Style.RESET_ALL}")
            
            return info

        except Exception as e:
            print(f"{Fore.RED}❌ Error obteniendo información: {str(e)}{Style.RESET_ALL}")
            return None

    def show_available_qualities(self):
        """Muestra las calidades disponibles"""
        qualities = ['best', '1080p', '720p', '480p', '360p', '240p', 'worst']
        print(f"{Fore.CYAN}🎥 Calidades disponibles:{Style.RESET_ALL}")
        for quality in qualities:
            print(f"  • {quality}")