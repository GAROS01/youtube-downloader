import os
import sys

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(__file__))

from colorama import Fore, Style, init
from downloader import Downloader
from info_video import VideoInfo

# Inicializar colorama
init()

def show_menu():
    """Muestra el menú principal"""
    print(f"\n{Fore.CYAN}{'='*55}")
    print("🎬 DESCARGADOR DE VIDEOS DE YOUTUBE")
    print(f"{'='*55}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Descargar video (yt-dlp) - Máxima calidad 🏆")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Descargar video (pytubefix) - Rápido 🚀")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} Descargar solo audio (MP3) - 320kbps 🎵")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} Obtener información del video 📊")
    print(f"{Fore.GREEN}5.{Style.RESET_ALL} Descargar múltiples videos 📦")
    print(f"{Fore.GREEN}6.{Style.RESET_ALL} Cambiar directorio de descarga 📁")
    print(f"{Fore.GREEN}7.{Style.RESET_ALL} Ver calidades disponibles 🎥")
    print(f"{Fore.GREEN}8.{Style.RESET_ALL} Descarga máxima calidad (separar+fusionar) 🎯")
    print(f"{Fore.RED}0.{Style.RESET_ALL} Salir 👋")
    print(f"{Fore.CYAN}{'='*55}{Style.RESET_ALL}")

def get_multiple_urls():
    """Obtiene múltiples URLs del usuario"""
    urls = []
    print(f"{Fore.CYAN}📝 Ingresa las URLs (presiona Enter sin texto para terminar):{Style.RESET_ALL}")
    
    while True:
        url = input(f"{Fore.YELLOW}URL {len(urls) + 1}: {Style.RESET_ALL}").strip()
        if not url:
            break
        urls.append(url)
    
    return urls

def main():
    print(f"{Fore.MAGENTA}🎉 Bienvenido al descargador de videos de YouTube{Style.RESET_ALL}")
    print(f"{Fore.CYAN}✨ Ahora con descarga en máxima calidad (video+audio separados){Style.RESET_ALL}")
    
    downloader = Downloader()
    video_info = VideoInfo()
    
    while True:
        show_menu()
        
        try:
            choice = input(f"\n{Fore.YELLOW}Selecciona una opción (0-8): {Style.RESET_ALL}").strip()
            
            if choice == '0':
                print(f"{Fore.MAGENTA}👋 ¡Gracias por usar el descargador! Adiós{Style.RESET_ALL}")
                break
                
            elif choice == '1':
                url = input(f"{Fore.CYAN}📎 Ingresa la URL del video: {Style.RESET_ALL}").strip()
                print(f"{Fore.YELLOW}🎥 Calidades disponibles: best, 2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, worst{Style.RESET_ALL}")
                quality = input(f"{Fore.CYAN}🎬 Calidad [best]: {Style.RESET_ALL}").strip() or 'best'
                downloader.download_video(url, quality)
                
            elif choice == '2':
                url = input(f"{Fore.CYAN}📎 Ingresa la URL del video: {Style.RESET_ALL}").strip()
                print(f"{Fore.YELLOW}🎥 Calidades disponibles: highest, 1080p, 720p, 480p, 360p, 240p, lowest{Style.RESET_ALL}")
                quality = input(f"{Fore.CYAN}🎬 Calidad [highest]: {Style.RESET_ALL}").strip() or 'highest'
                downloader.download_video_pytube(url, quality)
                
            elif choice == '3':
                url = input(f"{Fore.CYAN}📎 Ingresa la URL del video: {Style.RESET_ALL}").strip()
                downloader.download_video(url, audio_only=True)
                
            elif choice == '4':
                url = input(f"{Fore.CYAN}📎 Ingresa la URL del video: {Style.RESET_ALL}").strip()
                video_info.get_video_info(url)
                
            elif choice == '5':
                urls = get_multiple_urls()
                if urls:
                    print(f"{Fore.YELLOW}🎥 Calidades disponibles: best, 1080p, 720p, 480p, 360p, 240p, worst{Style.RESET_ALL}")
                    quality = input(f"{Fore.CYAN}🎬 Calidad para todos [best]: {Style.RESET_ALL}").strip() or 'best'
                    downloader.download_multiple_videos(urls, quality)
                else:
                    print(f"{Fore.YELLOW}⚠️ No se ingresaron URLs{Style.RESET_ALL}")
                
            elif choice == '6':
                new_path = input(f"{Fore.CYAN}📁 Nuevo directorio de descarga [{downloader.download_path}]: {Style.RESET_ALL}").strip()
                if new_path:
                    downloader.download_path = new_path
                    downloader.create_download_directory()
                    print(f"{Fore.GREEN}✅ Directorio cambiado a: {new_path}{Style.RESET_ALL}")
                    
            elif choice == '7':
                downloader.show_available_qualities()
                
            elif choice == '8':
                url = input(f"{Fore.CYAN}📎 Ingresa la URL del video: {Style.RESET_ALL}").strip()
                print(f"{Fore.CYAN}🎯 Esta opción descarga el mejor video + mejor audio y los combina{Style.RESET_ALL}")
                downloader.download_best_quality_separate(url)
                    
            else:
                print(f"{Fore.RED}❌ Opción no válida. Por favor, selecciona 0-8{Style.RESET_ALL}")
                
        except KeyboardInterrupt:
            print(f"\n{Fore.MAGENTA}👋 ¡Operación cancelada! Adiós{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}❌ Error inesperado: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()