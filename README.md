# 🎬 YouTube Downloader

Un descargador de videos de YouTube moderno y fácil de usar, desarrollado en Python con una interfaz de línea de comandos colorida e interactiva.

## ✨ Características

- 🎥 **Descarga videos** en diferentes calidades (1080p, 720p, 480p, 360p, etc.)
- 🎵 **Extrae audio** en formato MP3
- 📋 **Información detallada** del video (título, autor, duración, vistas)
- 🔄 **Dos motores de descarga**: yt-dlp (recomendado) y pytube
- 🎨 **Interfaz colorida** con emojis para mejor experiencia
- 📁 **Directorio personalizable** de descarga
- ✅ **Validación de URLs** de YouTube
- 🛡️ **Manejo robusto de errores**

## 📁 Estructura del Proyecto

```
youtube-downloader/
├── src/
│   ├── main.py              # Punto de entrada con menú interactivo
│   ├── downloader.py        # Clase principal para descargas
│   └── utils/
│       └── __init__.py      # Funciones utilitarias (validación, formato)
├── requirements.txt         # Dependencias del proyecto
├── setup.py                # Configuración del paquete
├── .venv/                  # Entorno virtual (creado localmente)
└── README.md               # Documentación del proyecto
```

## 🚀 Instalación

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd youtube-downloader
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar entorno virtual

**Windows:**

```bash
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🎯 Uso

### Ejecutar la aplicación

```bash
cd src
python main.py
```

### Menú de opciones

El programa presenta un menú interactivo con las siguientes opciones:

1. **Descargar video (yt-dlp)** - Método recomendado, más estable
2. **Descargar video (pytube)** - Método alternativo
3. **Descargar solo audio (MP3)** - Extrae únicamente el audio
4. **Obtener información del video** - Muestra detalles sin descargar
5. **Cambiar directorio de descarga** - Personaliza la carpeta destino
6. **Salir** - Cierra la aplicación

### Ejemplo de uso

```
🎬 DESCARGADOR DE VIDEOS DE YOUTUBE
==================================================
1. Descargar video (yt-dlp)
2. Descargar video (pytube)
3. Descargar solo audio (MP3)
4. Obtener información del video
5. Cambiar directorio de descarga
0. Salir
==================================================

Selecciona una opción (0-5): 1
📎 Ingresa la URL del video: https://www.youtube.com/watch?v=ejemplo
🎥 Calidad (best/worst/1080/720p/480p/360p) [best]: 720p
🔄 Descargando video...
✅ Descarga completada exitosamente
```

## 📦 Dependencias

- **yt-dlp** - Motor principal de descarga
- **pytube** - Motor alternativo de descarga
- **requests** - Peticiones HTTP
- **colorama** - Colores en terminal
- **tqdm** - Barras de progreso

## 🔧 Funcionalidades Técnicas

### Validación de URLs

El programa acepta los siguientes formatos de URL de YouTube:

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `https://www.youtube.com/v/VIDEO_ID`

### Formatos de Descarga

- **Video**: MP4 en diferentes resoluciones
- **Audio**: MP3 con calidad de 192 kbps
- **Calidades disponibles**: best, worst, 720p, 480p, 360p

### Gestión de Archivos

- Limpieza automática de nombres de archivo
- Creación automática de directorio de descarga
- Validación de caracteres especiales

## 🛠️ Desarrollo

### Instalación para desarrollo

```bash
pip install -e ".[dev]"
```

### Estructura de clases

- **Downloader**: Clase principal para gestión de descargas
- **validate_url()**: Función para validar URLs de YouTube
- **format_filename()**: Función para limpiar nombres de archivo

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de los cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🐛 Reporte de Problemas

Si encuentras algún problema, por favor abre un issue en el repositorio con:

- Descripción del problema
- Pasos para reproducir
- URL del video (si aplica)
- Mensaje de error completo

---

**Desarrollado por GarosDev** 🚀
