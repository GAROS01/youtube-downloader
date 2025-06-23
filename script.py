from yt_dlp import YoutubeDL


def descargar_video(url, formato="mp4"):
    # Opciones de descarga
    opciones = {
        "format": f"bestvideo[ext={formato}]+bestaudio[ext=m4a]/best[ext={formato}]",
        "outtmpl": "%(title)s.%(ext)s",  # Nombre del archivo de salida
    }

    try:
        # Crear el descargador
        with YoutubeDL(opciones) as ydl:
            # Descargar el video
            ydl.download([url])
        print("Descarga completada exitosamente")
    except Exception as e:
        print(f"Error al descargar: {str(e)}")


# URL del video a descargar
url = "Aqui va el link del video de youtube a descargar"
descargar_video(url)
