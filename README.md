# 🎬 YouTube Downloader

Un descargador de videos de YouTube moderno y fácil de usar, desarrollado en Python con una interfaz de línea de comandos

> 💡 **¿Buscas algo más simple?** Tenemos una versión más básica y sencilla disponible en: [https://github.com/GAROS01/YouTube-Download](https://github.com/GAROS01/YouTube-Download)

## ✨ Características

- 🎥 **Descarga videos** en diferentes calidades (4K, 1080p, 720p, 480p, 360p, etc.)
- 🎵 **Extrae audio** en formato MP3 de alta calidad (320 kbps)
- 🎯 **Máxima calidad disponible** combinando video y audio por separado
- 📊 **Barras de progreso avanzadas** con velocidad de descarga y tiempo estimado
- 📋 **Información detallada** del video con descripciones extensas
- 🔄 **Dos motores de descarga**: yt-dlp (recomendado) y pytubefix (actualizado)
- 📦 **Descarga múltiple** con progreso individual y general
- 🔄 **Descarga de playlists completas** automática con organización en carpetas
- 🎨 **Interfaz colorida** con emojis para mejor experiencia de usuario
- 📁 **Directorio personalizable** de descarga
- ✅ **Validación robusta** de URLs de YouTube
- 🛡️ **Manejo robusto de errores** con métodos de respaldo
- 🔍 **Análisis detallado** de streams disponibles con progreso visual
- 💡 **Vista previa** de descripciones con opción de ver contenido completo
- 🔧 **Detección automática de FFmpeg** para fusión de streams

## 🎯 Versiones Disponibles

| Versión             | Descripción                                                                            | Ideal para                                     | Enlace                                                                   |
| ------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------ |
| **Avanzada** (Esta) | Interfaz completa con múltiples opciones, máxima calidad, barras de progreso avanzadas | Usuarios que quieren todas las funcionalidades | Aquí mismo                                                               |
| **Simple**          | Script básico y directo, fácil de usar                                                 | Usuarios que prefieren simplicidad             | [GitHub - YouTube-Download](https://github.com/GAROS01/YouTube-Download) |

## 📁 Estructura del Proyecto

```
youtube-downloader/
├── src/
│   ├── main.py                # Punto de entrada con menú interactivo
│   ├── downloader.py          # Clase principal para descargas con máxima calidad
│   ├── info_video.py          # Clase para obtener información detallada de videos
│   └── utils/
│       └── __init__.py        # Funciones utilitarias (validación, formato)
├── downloads/                 # Directorio de descargas (creado automáticamente)
├── requirements.txt           # Dependencias del proyecto
├── setup.py                   # Configuración del paquete
├── LICENSE.md                 # Licencia MIT
└── README.md                  # Documentación del proyecto
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

1. **Descargar video (yt-dlp)** - Método recomendado, máxima calidad 🏆
2. **Descargar video (pytubefix)** - Método alternativo rápido 🚀
3. **Descargar solo audio (MP3)** - Extrae únicamente el audio a 320kbps 🎵
4. **Obtener información del video** - Muestra detalles completos sin descargar 📊
5. **Descargar múltiples videos** - Descarga varios videos en máxima calidad 🎯📦
6. **Descargar playlist completa** - Descarga automática de todas las playlists 🔄📑
7. **Cambiar directorio de descarga** - Personaliza la carpeta destino 📁
8. **Ver calidades disponibles** - Muestra todas las opciones de calidad 🎥
9. **Descarga máxima calidad (separar+fusionar)** - Combina mejor video + mejor audio 🎯
10. **Salir** - Cierra la aplicación 👋

### Ejemplo de uso con máxima calidad

```
🎬 DESCARGADOR DE VIDEOS DE YOUTUBE
=======================================================
1. Descargar video (yt-dlp) - Máxima calidad 🏆
2. Descargar video (pytubefix) - Rápido 🚀
3. Descargar solo audio (MP3) - 320kbps 🎵
4. Obtener información del video 📊
5. Descargar múltiples videos - Máxima calidad 🎯📦
6. Descargar playlist completa - Automático 🔄📑
7. Cambiar directorio de descarga 📁
8. Ver calidades disponibles 🎥
9. Descarga máxima calidad (separar+fusionar) 🎯
0. Salir 👋
=======================================================

Selecciona una opción (0-9): 1
📎 Ingresa la URL del video: https://www.youtube.com/watch?v=ejemplo
🎥 Calidades disponibles: best, 2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, worst
🎬 Calidad [best]: 1080p

🎬 Descargando video en calidad: 1080p...
📊 Formato: bestvideo[height<=?1080][height>720]+bestaudio/best[height<=?1080]
🔍 Analizando formatos disponibles...
📊 Formatos que se descargarán:
  🎥 Video: 1080p @ 30fps (avc1)
  🎵 Audio: 160kbps (mp4a)

📥 Descargando ████████████████████████████████████████ 100%  245.8M/245.8M [2.4MB/s]
✅ Descarga completada: Tutorial completo de Python 2024.mp4
🎉 Descarga completada exitosamente
📁 Guardado en: downloads
```

### Descarga múltiple en máxima calidad

```
Selecciona una opción (0-8): 5
� Ingresa las URLs (presiona Enter sin texto para terminar):
URL 1: https://www.youtube.com/watch?v=ejemplo1
URL 2: https://www.youtube.com/watch?v=ejemplo2
URL 3:

🎯 Esta opción descarga múltiples videos en máxima calidad (video+audio separados)
📊 Se usará la mejor calidad disponible para cada video
¿Continuar con la descarga en máxima calidad? (s/n): s

📦 Descargando 2 videos en máxima calidad...
🎯 Usando configuración de máxima calidad (video+audio separados)

📹 Descargando video 1/2 en máxima calidad
� URL: https://www.youtube.com/watch?v=ejemplo1
📹 Título: Tutorial completo de Python 2024...
  🎥 Video: 1080p @ 30fps
  🎵 Audio: 320kbps
�📥 Descargando ████████████████████████████████████████ 100%  245.8M/245.8M [2.4MB/s]
✅ Video 1 descargado exitosamente

📹 Descargando video 2/2 en máxima calidad
🔗 URL: https://www.youtube.com/watch?v=ejemplo2
📹 Título: JavaScript avanzado...
  🎥 Video: 1440p @ 60fps
  🎵 Audio: 320kbps
📥 Descargando ████████████████████████████████████████ 100%  892.3M/892.3M [3.1MB/s]
✅ Video 2 descargado exitosamente

============================================================
📊 RESUMEN DE DESCARGA MÚLTIPLE
============================================================
✅ Videos descargados exitosamente: 2/2

🎉 Descarga completada con máxima calidad
📁 Videos guardados en: downloads
💡 Todos los videos fueron descargados con la mejor calidad disponible (video+audio combinados)
============================================================
```

### Descarga de playlist completa automática

```
Selecciona una opción (0-9): 6
📎 Ingresa la URL de la playlist: https://www.youtube.com/playlist?list=PLxxxxxx
🔄 Esta opción descarga todos los videos de la playlist automáticamente
📊 Se usará la mejor calidad disponible para cada video
¿Continuar con la descarga de la playlist? (s/n): s

🔄 Analizando playlist...

📑 Playlist encontrada:
📋 Título: Python Tutorial Complete Course 2024
👤 Canal: TechChannel
🎬 Total de videos: 45
📁 Los videos se guardarán en: downloads/Python Tutorial Complete Course 2024

🚀 Iniciando descarga de playlist en máxima calidad...

📹 Descargando video 1/45 de la playlist
📹 1. Introduction to Python Programming...
  🎥 Video: 1080p @ 30fps
  🎵 Audio: 320kbps
📥 Descargando ████████████████████████████████████████ 100%  125.3M/125.3M [2.8MB/s]
✅ Video 1 descargado exitosamente

📹 Descargando video 2/45 de la playlist
📹 2. Variables and Data Types...
  🎥 Video: 1080p @ 30fps
  🎵 Audio: 320kbps
📥 Descargando ████████████████████████████████████████ 100%  98.7M/98.7M [3.1MB/s]
✅ Video 2 descargado exitosamente

============================================================
📊 RESUMEN DE DESCARGA DE PLAYLIST
============================================================
📋 Playlist: Python Tutorial Complete Course 2024
👤 Canal: TechChannel
✅ Videos descargados exitosamente: 43/45
❌ Videos que fallaron: 2

🎉 Descarga de playlist completada
📁 Videos guardados en: downloads/Python Tutorial Complete Course 2024
⭐ Descarga exitosa: 95.6% completado
============================================================
```

### Audio en máxima calidad

```
Selecciona una opción (0-9): 3
📎 Ingresa la URL del video: https://www.youtube.com/watch?v=ejemplo

🎵 Descargando audio en máxima calidad (320kbps MP3)...
📥 Descargando ████████████████████████████████████████ 100%  28.4M/28.4M [1.8MB/s]
🎵 Convirtiendo a MP3 320kbps...
✅ Descarga completada: Tutorial completo de Python 2024.mp3
🎉 Descarga completada exitosamente
📁 Guardado en: downloads
```

### Información de calidades disponibles

```
Selecciona una opción (0-9): 8

============================================================
🎥 CALIDADES Y MÉTODOS DE DESCARGA DISPONIBLES
============================================================
📱 Métodos de descarga:
  1️⃣ yt-dlp (🏆 RECOMENDADO) - Combina mejor video + mejor audio
  2️⃣ pytubefix - Streams progresivos (limitado pero rápido)

🎬 Calidades disponibles para yt-dlp:
  🏆 best     - Máxima calidad disponible (hasta 4K si está disponible)
  🎬 2160p    - 4K Ultra HD (si está disponible)
  📺 1440p    - 2K Quad HD (si está disponible)
  🎥 1080p    - Full HD - Combina video 1080p + mejor audio
  📱 720p     - HD - Perfecto para móviles y tablets
  💻 480p     - SD - Buena calidad, menor tamaño
  📞 360p     - Baja calidad - Para conexiones lentas
  ⚡ 240p     - Mínima calidad - Máximo ahorro de datos
  💾 worst    - Peor calidad disponible - Menor tamaño de archivo

🔧 Características de yt-dlp:
  ✅ Combina automáticamente video de alta calidad + audio de alta calidad
  ✅ Soporta formatos hasta 4K y audio hasta 320kbps
  ✅ Usa FFmpeg para fusionar streams (se instala automáticamente)
  ✅ Mejor compatibilidad con diferentes tipos de videos

📊 Características de pytubefix:
  ⚠️ Solo streams progresivos (video+audio en un solo archivo)
  ⚠️ Limitado a calidades que YouTube ofrece como progresivos
  ✅ Más rápido para obtener información del video
  ✅ No requiere FFmpeg

💡 Recomendaciones:
  🎯 Para máxima calidad: Usa yt-dlp con 'best' o '1080p'
  📱 Para dispositivos móviles: '720p' o '480p'
  💾 Para ahorrar espacio: '360p' o 'worst'
  🎵 Para solo audio: Usar opción 3 (MP3 a 320kbps)
============================================================
```

### Descarga en máxima calidad (Opción 9)

```
Selecciona una opción (0-9): 9
📎 Ingresa la URL del video: https://www.youtube.com/watch?v=ejemplo
🎯 Esta opción descarga el mejor video + mejor audio y los combina

🎯 Descarga en máxima calidad (video + audio separados)
📥 Descargando ████████████████████████████████████████ 100%  512.3M/512.3M [3.2MB/s]
✅ Descarga completada: Tutorial 4K Ultra HD.mp4
🎉 Descarga completada exitosamente
📁 Guardado en: downloads
```

## 📦 Dependencias

- **yt-dlp >=2025.6.9** - Motor principal de descarga, más estable y actualizado
- **pytubefix >=8.8.4** - Motor alternativo actualizado (reemplaza pytube)
- **requests >=2.31.0** - Peticiones HTTP
- **colorama >=0.4.6** - Colores en terminal
- **tqdm >=4.67.1** - Barras de progreso avanzadas con velocidad y tiempo estimado
- **FFmpeg** - Fusión de streams de video y audio (se instala automáticamente por yt-dlp)

## 🎨 Características Visuales

### Barras de Progreso Avanzadas

- **Velocidad de descarga**: Muestra MB/s en tiempo real
- **Progreso visual**: Barras coloridas con porcentajes
- **Tiempo estimado**: Cálculo automático del tiempo restante
- **Tamaño del archivo**: Descargado/Total en formato legible
- **Múltiples procesos**: Progreso individual y general para descargas múltiples

### Análisis de Formatos

```
🔍 Analizando formatos disponibles...
📊 Formatos que se descargarán:
  🎥 Video: 1080p @ 60fps (avc1)
  🎵 Audio: 320kbps (mp4a)
```

### Detección de FFmpeg

```
🔧 FFmpeg detectado ✅ - Fusión de streams habilitada
🎯 Máxima calidad disponible: Video 4K + Audio 320kbps
```

## 🔧 Funcionalidades Técnicas

### Validación de URLs

El programa acepta los siguientes formatos de URL de YouTube:

**Videos individuales:**

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `https://www.youtube.com/v/VIDEO_ID`

**Playlists:**

- `https://www.youtube.com/playlist?list=PLAYLIST_ID`
- `https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID`
- `https://www.youtube.com/watch?list=PLAYLIST_ID`

### Formatos de Descarga Mejorados

#### Video (yt-dlp)

- **4K (2160p)**: Hasta 4K Ultra HD + Audio 320kbps
- **2K (1440p)**: Quad HD + Audio 320kbps
- **Full HD (1080p)**: 1080p + Audio 320kbps
- **HD (720p)**: 720p + Audio 320kbps
- **SD (480p, 360p, 240p)**: Calidades estándar

#### Audio

- **MP3**: 320kbps (máxima calidad)
- **Formato original**: Mantiene codec original cuando es posible

### Características Avanzadas de Calidad

- **Fusión de streams**: Combina automáticamente el mejor video + mejor audio
- **Detección de FFmpeg**: Verifica disponibilidad para fusión de streams
- **Selección inteligente**: Elige los mejores formatos disponibles
- **Fallback automático**: Si falla la fusión, usa stream progresivo
- **Información de formatos**: Muestra qué calidades serán descargadas
- **Verificación de calidad**: Confirma que se descarga la calidad solicitada

### Configuraciones de Formato

#### Máxima Calidad (yt-dlp)

```
best: bestvideo[height<=?1080]+bestaudio/best[height<=?1080]
1080p: bestvideo[height<=?1080][height>720]+bestaudio/best[height<=?1080]
720p: bestvideo[height<=?720][height>480]+bestaudio/best[height<=?720]
```

#### Fusión Automática

- Descarga video de máxima calidad disponible
- Descarga audio de máxima calidad disponible
- Fusiona automáticamente con FFmpeg
- Resultado: Archivo MP4 con máxima calidad de video y audio

## 🔄 Métodos de Descarga Actualizados

### yt-dlp (Recomendado) 🏆

- ✅ **Máxima calidad**: Combina mejor video + mejor audio
- ✅ **Soporta 4K**: Hasta 2160p cuando está disponible
- ✅ **Audio 320kbps**: Máxima calidad de audio
- ✅ **Fusión automática**: Usa FFmpeg para combinar streams
- ✅ **Más estable**: Mejor manejo de restricciones
- ✅ **Actualizaciones frecuentes**: Siempre compatible
- ✅ **Formatos específicos**: Garantiza la calidad solicitada

### pytubefix (Alternativo) 🚀

- ✅ **Rápido**: Descarga directa de streams progresivos
- ✅ **Simple**: No requiere FFmpeg
- ✅ **Información rápida**: Análisis veloz de videos
- ⚠️ **Limitado**: Solo streams que YouTube ofrece como progresivos
- ⚠️ **Calidad limitada**: Máximo 720p en la mayoría de casos

### Recomendaciones de Uso

| Necesidad      | Método Recomendado | Calidad           | Motivo                       |
| -------------- | ------------------ | ----------------- | ---------------------------- |
| Máxima calidad | yt-dlp             | `best` o `1080p`  | Combina mejor video + audio  |
| 4K/2K          | yt-dlp             | `2160p` o `1440p` | Solo disponible en yt-dlp    |
| Velocidad      | pytubefix          | `highest`         | Descarga directa             |
| Audio          | yt-dlp             | Audio only        | MP3 320kbps                  |
| Móvil          | Cualquiera         | `720p` o `480p`   | Ambos métodos funcionan bien |

## 🛠️ Desarrollo

### Instalación para desarrollo

```bash
pip install -e ".[dev]"
```

### Estructura de clases actualizadas

- **Downloader**: Clase principal con métodos de máxima calidad
  - `download_video()`: Descarga con configuración mejorada de yt-dlp y pytubefix
  - `download_best_quality_separate()`: Máxima calidad separando streams (bestvideo+bestaudio)
  - `download_multiple_videos()`: Descarga múltiple con máxima calidad automática
  - `download_playlist()`: Descarga automática de playlists completas con organización
  - `progress_hook()`: Sistema de progreso mejorado con información detallada
  - `show_available_qualities()`: Información completa de métodos y calidades
  - `create_download_directory()`: Gestión automática de directorios
- **VideoInfo**: Información detallada con análisis de calidades
- **validate_url()**: Validación robusta de URLs de YouTube (videos y playlists)
- **format_filename()**: Limpieza de nombres de archivo y carpetas

### Nuevas Características Técnicas

- **Configuración de formatos optimizada**: Garantiza máxima calidad con `bestvideo+bestaudio/best`
- **Descarga múltiple mejorada**: Progreso individual y resumen detallado por video
- **Descarga de playlists completas**: Extracción automática de todas las URLs con organización en carpetas
- **Información de streams en tiempo real**: Muestra resolución, fps y bitrate antes de descargar
- **Gestión robusta de errores**: Manejo individual de fallos en descargas múltiples y playlists
- **Progreso visual avanzado**: Barras de progreso con velocidad y tamaño de archivo
- **Resumen de descargas**: Estadísticas completas de éxito y fallos en descargas múltiples
- **Organización automática**: Playlists se guardan en carpetas con nombres descriptivos
- **Numeración secuencial**: Videos de playlist numerados según su orden original

## 🎨 Interfaz de Usuario Mejorada

- **Nuevos iconos**: Diferenciación visual de métodos de calidad
- **Información de formatos**: Muestra configuración técnica
- **Advertencias inteligentes**: Informa sobre limitaciones
- **Progreso detallado**: Múltiples fases claramente mostradas
- **Colores específicos**: Diferentes colores para cada tipo de información

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/MaxQuality`)
3. Commit de los cambios (`git commit -m 'Add MaxQuality feature'`)
4. Push a la rama (`git push origin feature/MaxQuality`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🐛 Reporte de Problemas

Si encuentras algún problema, por favor abre un issue con:

- URL del video que falla
- Calidad solicitada
- Método de descarga utilizado (yt-dlp o pytubefix)
- Mensaje de error completo
- Información del sistema operativo
- Versión de yt-dlp/pytubefix instalada

## 🔗 Proyectos Relacionados

- **[YouTube-Download (Simple)](https://github.com/GAROS01/YouTube-Download)** - Versión más básica y directa, ideal para uso rápido y sencillo

---

**Desarrollado por GarosDev** 🚀

_VibeCoding_

