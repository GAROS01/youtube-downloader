import yt_dlp
from pytube import YouTube
from colorama import Fore, Style, init
from utils import validate_url

# Inicializar colorama para Windows
init()

class VideoInfo:
    def __init__(self):
        pass

    def get_video_info(self, url):
        """Obtiene información del video usando yt-dlp (método principal)"""
        if not validate_url(url):
            print(f"{Fore.RED}❌ URL no válida: {url}{Style.RESET_ALL}")
            return None

        try:
            print(f"{Fore.CYAN}🔄 Obteniendo información del video...{Style.RESET_ALL}")
            
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
                        qualities.add(f"{fmt['height']}p")
                
                # Mostrar información
                self._display_video_info(info, duration_str, qualities)
                
                return {
                    'title': info.get('title', 'N/A'),
                    'uploader': info.get('uploader', 'N/A'),
                    'duration': duration_str,
                    'view_count': info.get('view_count', 0),
                    'upload_date': info.get('upload_date', 'N/A'),
                    'description': info.get('description', ''),
                    'qualities': sorted([int(q.replace('p', '')) for q in qualities if q.replace('p', '').isdigit()], reverse=True)
                }

        except Exception as e:
            print(f"{Fore.RED}❌ Error obteniendo información con yt-dlp: {str(e)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}🔄 Intentando con método alternativo...{Style.RESET_ALL}")
            return self.get_video_info_pytube(url)

    def get_video_info_pytube(self, url):
        """Obtiene información del video usando pytube (método alternativo)"""
        try:
            yt = YouTube(url)
            
            # Formatear duración
            duration_str = f"{yt.length // 60}:{yt.length % 60:02d}" if yt.length else "Desconocido"
            
            # Obtener calidades disponibles
            streams = yt.streams.filter(progressive=True, file_extension='mp4')
            qualities = [int(stream.resolution.replace('p', '')) for stream in streams if stream.resolution]
            qualities = sorted(list(set(qualities)), reverse=True)
            
            print(f"{Fore.GREEN}📋 Información del video:{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📹 Título: {yt.title}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}👤 Autor: {yt.author}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}⏱️ Duración: {duration_str}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}👁️ Vistas: {yt.views:,}{Style.RESET_ALL}")
            
            if qualities:
                qualities_str = ', '.join([f"{q}p" for q in qualities])
                print(f"{Fore.YELLOW}🎥 Calidades disponibles: {qualities_str}{Style.RESET_ALL}")
            
            if yt.description:
                desc_preview = yt.description[:200] + '...' if len(yt.description) > 200 else yt.description
                print(f"{Fore.YELLOW}📝 Descripción: {desc_preview}{Style.RESET_ALL}")
            
            return {
                'title': yt.title,
                'uploader': yt.author,
                'duration': duration_str,
                'view_count': yt.views,
                'upload_date': 'N/A',
                'description': yt.description,
                'qualities': qualities
            }
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error obteniendo información con pytube: {str(e)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 Intenta con la opción de descarga directa{Style.RESET_ALL}")
            return None

    def _display_video_info(self, info, duration_str, qualities):
        """Muestra la información del video de forma organizada"""
        print(f"{Fore.GREEN}📋 Información del video:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📹 Título: {info.get('title', 'N/A')}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}👤 Autor: {info.get('uploader', 'N/A')}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}⏱️ Duración: {duration_str}{Style.RESET_ALL}")
        
        view_count = info.get('view_count')
        if view_count:
            print(f"{Fore.YELLOW}👁️ Vistas: {view_count:,}{Style.RESET_ALL}")
        
        upload_date = info.get('upload_date')
        if upload_date:
            # Formatear fecha (YYYYMMDD -> DD/MM/YYYY)
            if len(upload_date) == 8:
                formatted_date = f"{upload_date[6:8]}/{upload_date[4:6]}/{upload_date[:4]}"
                print(f"{Fore.YELLOW}📅 Fecha de subida: {formatted_date}{Style.RESET_ALL}")
        
        if qualities:
            qualities_sorted = sorted([int(q.replace('p', '')) for q in qualities if q.replace('p', '').isdigit()], reverse=True)
            qualities_str = ', '.join([f"{q}p" for q in qualities_sorted])
            print(f"{Fore.YELLOW}🎥 Calidades disponibles: {qualities_str}{Style.RESET_ALL}")
        
        description = info.get('description', '')
        if description:
            desc_preview = description[:200] + '...' if len(description) > 200 else description
            print(f"{Fore.YELLOW}📝 Descripción: {desc_preview}{Style.RESET_ALL}")

    def show_available_qualities(self):
        """Muestra las calidades disponibles para descarga"""
        qualities = ['best', '1080p', '720p', '480p', '360p', '240p', 'worst']
        print(f"{Fore.CYAN}🎥 Calidades disponibles para descarga:{Style.RESET_ALL}")
        for quality in qualities:
            print(f"  • {quality}")