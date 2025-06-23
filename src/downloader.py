import os
import yt_dlp
from pytube import YouTube
from colorama import Fore, Style, init
from tqdm import tqdm
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
            # Configuración de yt-dlp
            ydl_opts = {
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'format': 'bestaudio/best' if audio_only else quality,
            }

            if audio_only:
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            print(f"{Fore.CYAN}🔄 Descargando video...{Style.RESET_ALL}")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            print(f"{Fore.GREEN}✅ Descarga completada exitosamente{Style.RESET_ALL}")
            return True

        except Exception as e:
            print(f"{Fore.RED}❌ Error durante la descarga: {str(e)}{Style.RESET_ALL}")
            return False

    def download_video_pytube(self, url, quality='highest'):
        """Descarga video usando pytube (alternativo)"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return False

        try:
            print(f"{Fore.CYAN}🔄 Obteniendo información del video...{Style.RESET_ALL}")
            yt = YouTube(url)
            
            # Seleccionar stream
            if quality == 'highest':
                stream = yt.streams.get_highest_resolution()
            elif quality == 'lowest':
                stream = yt.streams.get_lowest_resolution()
            else:
                stream = yt.streams.filter(res=quality).first()
                if not stream:
                    stream = yt.streams.get_highest_resolution()

            print(f"{Fore.YELLOW}📹 Título: {yt.title}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}🎥 Calidad: {stream.resolution}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}🔄 Descargando...{Style.RESET_ALL}")

            # Descargar
            stream.download(output_path=self.download_path)
            
            print(f"{Fore.GREEN}✅ Descarga completada exitosamente{Style.RESET_ALL}")
            return True

        except Exception as e:
            print(f"{Fore.RED}❌ Error durante la descarga: {str(e)}{Style.RESET_ALL}")
            return False

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