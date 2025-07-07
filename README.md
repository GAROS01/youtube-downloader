# 🎬 YouTube Downloader Pro

Un descargador de videos de YouTube profesional con interfaz de línea de comandos, optimizado para obtener la máxima calidad disponible.

> 💡 **¿Buscas algo más simple?** Tenemos una versión básica disponible en: [YouTube-Download](https://github.com/GAROS01/YouTube-Download)

## ✨ Características Principales

- 🎥 **Descarga en máxima calidad** hasta 4K (2160p) combinando video y audio por separado
- 🎵 **Audio premium** en MP3 a 320kbps de máxima calidad
- 🎯 **Fusión automática** de streams usando FFmpeg para calidad superior
- 📊 **Barras de progreso profesionales** con velocidad en tiempo real y ETA
- � **Descarga múltiple inteligente** con gestión de errores individualizada
- 🔄 **Playlists completas** con organización automática en carpetas
- 🎨 **Interfaz moderna** con colores y emojis para mejor UX
- 📁 **Gestión avanzada** de directorios y nombres de archivo
- ✅ **Validación robusta** de URLs (videos individuales y playlists)
- 🛡️ **Sistema de respaldo** con múltiples motores de descarga
- 🔍 **Análisis detallado** de formatos disponibles antes de descargar
- 🔧 **Detección automática** de dependencias (FFmpeg)

## 🎯 Comparación de Versiones

| Característica          | **Pro** (Esta versión)    | **Simple**                                                      |
| ----------------------- | ------------------------- | --------------------------------------------------------------- |
| **Interfaz**            | Menú interactivo completo | Script directo básico                                           |
| **Calidad máxima**      | ✅ 4K + Audio 320kbps     | ⚠️ Limitado a 1080p                                             |
| **Múltiples descargas** | ✅ Con progreso avanzado  | ❌ Solo videos únicos                                           |
| **Playlists**           | ✅ Automático completo    | ❌ No soportado                                                 |
| **Motores de descarga** | ✅ yt-dlp + pytubefix     | ⚠️ Solo pytube básico                                           |
| **Fusión de streams**   | ✅ Automática con FFmpeg  | ❌ Solo streams simples                                         |
| **Gestión de errores**  | ✅ Robusta y detallada    | ⚠️ Básica                                                       |
| **Ideal para**          | Usuarios avanzados        | Uso rápido y simple                                             |
| **Enlace**              | Aquí mismo                | [YouTube-Download](https://github.com/GAROS01/YouTube-Download) |

## 📁 Arquitectura del Proyecto

```
youtube-downloader/
├── 📂 src/                    # Código fuente principal
│   ├── 🎯 main.py             # Punto de entrada con menú interactivo
│   ├── ⬇️ downloader.py       # Motor de descarga con máxima calidad
│   ├── 📊 info_video.py       # Análisis detallado de videos
│   └── 📂 utils/              # Utilidades y funciones helper
│       └── __init__.py        # Validación de URLs y formateo
├── 📥 downloads/              # Directorio de descargas (auto-creado)
├── 📋 requirements.txt        # Dependencias del proyecto
├── 📄 LICENSE.md              # Licencia MIT
└── 📖 README.md               # Documentación completa
```

## 🚀 Instalación Rápida

### Opción 1: Instalación Automática (Recomendado)

```powershell
# Clonar el repositorio
git clone <url-del-repositorio>
cd youtube-downloader

# Crear e instalar automáticamente
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Opción 2: Instalación Manual

**1. Descargar/Clonar el proyecto:**

```powershell
git clone <url-del-repositorio>
cd youtube-downloader
```

**2. Crear entorno virtual:**

```powershell
python -m venv .venv
```

**3. Activar entorno virtual:**

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
.\.venv\Scripts\activate.bat
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

**4. Instalar dependencias:**

```powershell
pip install -r requirements.txt
```

## ⚡ Inicio Rápido

```powershell
cd src
python main.py
```

El programa se iniciará con un menú interactivo que te guiará paso a paso.

## 🎮 Guía de Uso Completa

### 🎯 Menú Principal

Al ejecutar el programa verás un menú interactivo moderno:

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
```

### 🏆 Descarga en Máxima Calidad (Opción 1 - Recomendada)

**Entrada:**

```
Selecciona una opción (0-9): 1
📎 Ingresa la URL del video: https://www.youtube.com/watch?v=ejemplo
🎥 Calidades disponibles: best, 2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, worst
🎬 Calidad [best]: 1080p
```

**Proceso de descarga:**

```
🎬 Descargando video en calidad: 1080p...
📊 Configuración: bestvideo[height<=?1080]+bestaudio/best[height<=?1080]
🔍 Analizando formatos disponibles...

📊 Formatos seleccionados:
  🎥 Video: 1080p @ 60fps (avc1) - 245.8MB
  🎵 Audio: 320kbps (mp4a) - 28.4MB

📥 Descargando ████████████████████████████████████████ 100% 274.2M/274.2M [3.2MB/s]
🔧 Fusionando video y audio con FFmpeg...
✅ Descarga completada: Tutorial Python Avanzado 2024.mp4

🎉 Descarga completada exitosamente
📁 Guardado en: downloads
💾 Tamaño final: 274.2MB | Calidad: 1080p60 + Audio 320kbps
```

### 📦 Descarga Múltiple Inteligente (Opción 5)

**Configuración:**

```
Selecciona una opción (0-9): 5
📝 Ingresa las URLs (presiona Enter sin texto para terminar):
URL 1: https://www.youtube.com/watch?v=video1
URL 2: https://www.youtube.com/watch?v=video2
URL 3: https://www.youtube.com/watch?v=video3
URL 4: [Enter sin texto]

🎯 Modo: Descarga múltiple en máxima calidad
📊 Total de videos: 3
¿Continuar con la descarga en máxima calidad? (s/n): s
```

**Proceso automático:**

```
📦 Iniciando descarga múltiple en máxima calidad...
🎯 Configuración: bestvideo+bestaudio para cada video

📹 [1/3] Descargando: Tutorial Python Básico
  🎥 Video: 1080p @ 30fps | 🎵 Audio: 320kbps
  📥 ████████████████████████████████████████ 100% 158.2M [2.8MB/s]
  ✅ Completado exitosamente

📹 [2/3] Descargando: JavaScript Avanzado
  🎥 Video: 1440p @ 60fps | 🎵 Audio: 320kbps
  � ████████████████████████████████████████ 100% 421.7M [3.1MB/s]
  ✅ Completado exitosamente

📹 [3/3] Descargando: React Hooks Tutorial
  🎥 Video: 1080p @ 30fps | 🎵 Audio: 320kbps
  📥 ████████████████████████████████████████ 100% 203.4M [2.9MB/s]
  ✅ Completado exitosamente

============================================================
📊 RESUMEN DE DESCARGA MÚLTIPLE
============================================================
✅ Videos exitosos: 3/3 (100%)
❌ Videos fallidos: 0/3 (0%)
💾 Tamaño total: 783.3MB
⏱️ Tiempo total: 4m 32s
📁 Ubicación: downloads/

🎉 ¡Descarga múltiple completada con éxito!
============================================================
```

### 🔄 Descarga de Playlist Completa (Opción 6)

**Configuración:**

```
Selecciona una opción (0-9): 6
📎 URL de la playlist: https://www.youtube.com/playlist?list=PLxxxxxx
```

**Análisis automático:**

```
🔄 Analizando playlist...

📑 Playlist detectada:
📋 Título: "Curso Completo de Python 2024"
👤 Canal: TechEdu Academy
🎬 Videos encontrados: 25
📁 Carpeta: downloads/Curso Completo de Python 2024/

¿Continuar con descarga automática en máxima calidad? (s/n): s
```

**Descarga automatizada:**

```
🚀 Iniciando descarga automática de playlist...

📹 [01/25] 1. Introducción a Python
  🎥 1080p @ 30fps | 🎵 320kbps | 📥 142.3MB
  ✅ 01 - Introducción a Python.mp4

📹 [02/25] 2. Variables y Tipos de Datos
  🎥 1080p @ 30fps | 🎵 320kbps | 📥 167.8MB
  ✅ 02 - Variables y Tipos de Datos.mp4

[...progreso continúa...]

📹 [25/25] 25. Proyecto Final
  🎥 1080p @ 60fps | 🎵 320kbps | 📥 389.2MB
  ✅ 25 - Proyecto Final.mp4

============================================================
📊 RESUMEN DE PLAYLIST
============================================================
📋 Playlist: "Curso Completo de Python 2024"
👤 Canal: TechEdu Academy
✅ Videos exitosos: 24/25 (96%)
❌ Videos fallidos: 1/25 (4%) - Video privado
💾 Tamaño total: 4.2GB
📁 Organización: Numeración automática secuencial
🎯 Calidad: Máxima disponible para cada video

🎉 ¡Playlist descargada y organizada exitosamente!
============================================================
```

### 🎵 Audio Premium MP3 (Opción 3)

**Descarga optimizada de audio:**

```
Selecciona una opción (0-9): 3
📎 URL del video: https://www.youtube.com/watch?v=ejemplo

🎵 Extrayendo audio en máxima calidad...
📊 Configuración: bestaudio/best > MP3 320kbps
🔍 Analizando formatos de audio disponibles...

🎵 Audio seleccionado:
  🎶 Formato: MP3 320kbps
  📏 Duración: 45:32
  💾 Tamaño estimado: 83.2MB

📥 Descargando ████████████████████████████████████████ 100% 83.2MB [2.1MB/s]
🔧 Convirtiendo a MP3 320kbps...
✅ Audio extraído: Tutorial Python Avanzado 2024.mp3

🎉 Extracción de audio completada
📁 Guardado en: downloads
🎶 Calidad: MP3 320kbps | Duración: 45:32
```

### 📊 Información Detallada del Video (Opción 4)

**Análisis completo sin descargar:**

```
Selecciona una opción (0-9): 4
📎 URL del video: https://www.youtube.com/watch?v=ejemplo

🔍 Analizando video...

============================================================
📊 INFORMACIÓN DETALLADA DEL VIDEO
============================================================
📹 Título: "Tutorial Completo de Python para Principiantes 2024"
👤 Canal: TechEdu Academy
📅 Fecha de subida: 15 de enero, 2024
👀 Visualizaciones: 1,234,567
👍 Likes: 45,678 | 👎 Dislikes: 1,234
📏 Duración: 2:34:15

📝 Descripción:
En este tutorial completo aprenderás Python desde cero...
[Mostrar descripción completa] (s/n): s

🎥 FORMATOS DE VIDEO DISPONIBLES:
┌─────────┬─────────────┬─────────┬──────────┬─────────┐
│ Calidad │ Resolución  │ FPS     │ Codec    │ Tamaño  │
├─────────┼─────────────┼─────────┼──────────┼─────────┤
│ 4K      │ 3840x2160   │ 30fps   │ avc1     │ 2.1GB   │
│ 1440p   │ 2560x1440   │ 60fps   │ vp9      │ 1.2GB   │
│ 1080p   │ 1920x1080   │ 60fps   │ avc1     │ 657MB   │
│ 720p    │ 1280x720    │ 30fps   │ avc1     │ 298MB   │
│ 480p    │ 854x480     │ 30fps   │ avc1     │ 156MB   │
└─────────┴─────────────┴─────────┴──────────┴─────────┘

🎵 FORMATOS DE AUDIO DISPONIBLES:
┌──────────┬─────────┬─────────┬─────────┐
│ Calidad  │ Bitrate │ Codec   │ Tamaño  │
├──────────┼─────────┼─────────┼─────────┤
│ Premium  │ 320kbps │ mp4a    │ 58.7MB  │
│ Alta     │ 160kbps │ mp4a    │ 29.4MB  │
│ Media    │ 128kbps │ mp4a    │ 23.5MB  │
└──────────┴─────────┴─────────┴─────────┘

� RECOMENDACIONES:
🏆 Máxima calidad: 4K + Audio 320kbps (Tamaño: ~2.16GB)
⚖️ Equilibrio: 1080p60 + Audio 320kbps (Tamaño: ~716MB)
📱 Móvil: 720p + Audio 160kbps (Tamaño: ~328MB)
============================================================
```

## 🔧 Tecnologías y Dependencias

### 📦 Stack Tecnológico

| Componente    | Versión   | Función                                    |
| ------------- | --------- | ------------------------------------------ |
| **yt-dlp**    | ≥2025.6.9 | Motor principal - máxima calidad y fusión  |
| **pytubefix** | ≥8.8.4    | Motor alternativo - velocidad optimizada   |
| **requests**  | ≥2.31.0   | Manejo de peticiones HTTP robustas         |
| **colorama**  | ≥0.4.6    | Interfaz colorida multiplataforma          |
| **tqdm**      | ≥4.67.1   | Barras de progreso profesionales           |
| **FFmpeg**    | Auto      | Fusión de streams (instalación automática) |

### ⚙️ Configuraciones Avanzadas de Descarga

#### 🏆 yt-dlp (Motor Recomendado)

**Configuraciones de formato optimizadas:**

```python
# Máxima calidad disponible
format: "bestvideo+bestaudio/best"

# 4K específico
format: "bestvideo[height<=2160]+bestaudio/best[height<=2160]"

# 1080p optimizado
format: "bestvideo[height<=1080][height>720]+bestaudio/best[height<=1080]"

# Audio premium
format: "bestaudio[ext=m4a]/bestaudio/best"
```

**Características técnicas:**

- ✅ **Fusión automática**: Video + Audio independientes para máxima calidad
- ✅ **Códecs avanzados**: Soporte AV1, VP9, H.264, H.265
- ✅ **HDR**: Soporte para contenido HDR cuando está disponible
- ✅ **Multi-stream**: Descarga paralela para mejor velocidad
- ✅ **Metadata**: Preserva información completa del video
- ✅ **Subtítulos**: Descarga automática cuando están disponibles

#### 🚀 pytubefix (Motor Alternativo)

**Ventajas específicas:**

- ⚡ **Velocidad**: Análisis más rápido de información
- 🔄 **Simplicidad**: Streams progresivos directos
- 📱 **Compatibilidad**: Mejor para dispositivos de recursos limitados
- 🛡️ **Estabilidad**: Menos dependencias externas

**Limitaciones conocidas:**

- ⚠️ **Calidad limitada**: Máximo 720p-1080p en muchos casos
- ⚠️ **Sin fusión**: No combina streams separados
- ⚠️ **Códecs limitados**: Solo formatos que YouTube ofrece como progresivos

## 🎨 Características de Interfaz

### 🌈 Sistema Visual Avanzado

- **🎯 Códigos de color**: Diferentes colores para cada tipo de información
- **📊 Barras de progreso**: Animadas con velocidad y ETA en tiempo real
- **🎭 Emojis contextuales**: Indicadores visuales para mejor UX
- **📋 Tablas formateadas**: Información organizada y fácil de leer
- **🔍 Análisis visual**: Progreso de análisis de formatos disponibles
- **� Estadísticas detalladas**: Resúmenes completos post-descarga

### 📋 Validación Robusta de URLs

**URLs soportadas para videos:**

```
✅ https://www.youtube.com/watch?v=VIDEO_ID
✅ https://youtu.be/VIDEO_ID
✅ https://www.youtube.com/embed/VIDEO_ID
✅ https://m.youtube.com/watch?v=VIDEO_ID
✅ https://youtube.com/watch?v=VIDEO_ID
```

**URLs soportadas para playlists:**

```
✅ https://www.youtube.com/playlist?list=PLAYLIST_ID
✅ https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID
✅ https://youtube.com/playlist?list=PLAYLIST_ID
```

### 🔄 Gestión Inteligente de Errores

**Estrategias de recuperación:**

- 🔄 **Reintentos automáticos**: 3 intentos por video con delays progresivos
- 🎯 **Fallback de motores**: Si falla yt-dlp, intenta con pytubefix
- 📋 **Logs detallados**: Registro completo de errores para debugging
- ✅ **Continuación de descargas**: Las descargas múltiples continúan aunque fallen algunas
- 🛡️ **Validación previa**: Verificación de URLs antes de iniciar descargas

## 🏗️ Arquitectura del Código

### � Estructura Modular

```python
src/
├── 🎯 main.py              # Interfaz principal y menú interactivo
├── ⬇️ downloader.py        # Lógica de descarga y configuraciones
├── 📊 info_video.py        # Análisis y extracción de metadatos
└── utils/
    └── __init__.py         # Utilidades, validación y formateo
```

### 🔧 Clases Principales

**Downloader Class:**

```python
class Downloader:
    - download_video()              # Descarga con yt-dlp/pytubefix
    - download_best_quality()       # Máxima calidad con fusión
    - download_multiple_videos()    # Descarga múltiple inteligente
    - download_playlist()           # Playlists completas automáticas
    - download_audio_only()         # Extracción de audio MP3 320kbps
    - progress_hook()              # Sistema de progreso avanzado
    - show_available_qualities()    # Información de formatos
```

**VideoInfo Class:**

```python
class VideoInfo:
    - get_video_info()             # Metadatos completos del video
    - analyze_formats()            # Análisis de calidades disponibles
    - get_playlist_info()          # Información de playlists
    - display_detailed_info()      # Presentación formateada
```

**Utils Functions:**

```python
def validate_url()                 # Validación robusta de URLs
def format_filename()              # Limpieza de nombres de archivo
def create_safe_directory()        # Creación segura de directorios
def format_bytes()                 # Conversión de tamaños legibles
```

## 💡 Casos de Uso y Recomendaciones

### 🎯 Guía de Selección de Calidad

| Uso Previsto             | Calidad Recomendada | Motor      | Tamaño Aproximado | Tiempo de Descarga |
| ------------------------ | ------------------- | ---------- | ----------------- | ------------------ |
| **Presentaciones 4K**    | `best` o `2160p`    | yt-dlp     | 1.5-3GB/hora      | 15-30 min          |
| **Streaming en casa**    | `1080p60`           | yt-dlp     | 500MB-1GB/hora    | 5-15 min           |
| **Dispositivos móviles** | `720p`              | Cualquiera | 200-400MB/hora    | 2-8 min            |
| **Conexión limitada**    | `480p`              | pytubefix  | 100-200MB/hora    | 1-4 min            |
| **Solo audio/música**    | Audio MP3           | yt-dlp     | 40-80MB/hora      | 30s-2 min          |

### 🚀 Optimización de Rendimiento

**Para conexiones rápidas (>50 Mbps):**

- Usar yt-dlp con máxima calidad
- Descargas múltiples de hasta 5 videos simultáneos
- Playlists completas en modo automático

**Para conexiones limitadas (<10 Mbps):**

- Usar pytubefix para videos únicos
- Calidades 720p o menor
- Evitar descargas múltiples

**Para almacenamiento limitado:**

- Audio MP3 para música/podcasts
- Calidades 480p-720p para videos
- Usar información de video (Opción 4) para verificar tamaños

## 🔧 Resolución de Problemas

### ❌ Problemas Comunes y Soluciones

**🚫 "Video no disponible o privado"**

```
Posibles causas:
- Video eliminado o privado
- Restricciones geográficas
- Video solo para miembros

Soluciones:
✅ Verificar que el video sea público
✅ Intentar con VPN si hay restricciones geográficas
✅ Probar con el motor alternativo (pytubefix)
```

**⚠️ "FFmpeg no encontrado"**

```
Síntomas:
- No se pueden fusionar streams de máxima calidad
- Solo descarga video o audio por separado

Soluciones:
✅ yt-dlp instala FFmpeg automáticamente
✅ Reiniciar el programa después de la primera descarga
✅ Verificar instalación con Opción 8 (Ver calidades)
```

**🐌 "Descarga muy lenta"**

```
Posibles causas:
- Servidor de YouTube congestionado
- Conexión a internet limitada
- Formato de alta calidad seleccionado

Soluciones:
✅ Cambiar a pytubefix para mejor velocidad
✅ Reducir calidad (720p en lugar de 1080p)
✅ Intentar en horarios de menor tráfico
✅ Verificar velocidad de internet
```

**📁 "Error de permisos de escritura"**

```
Síntomas:
- No se puede crear carpeta downloads
- Archivos no se guardan correctamente

Soluciones:
✅ Ejecutar como administrador
✅ Cambiar directorio de descarga (Opción 7)
✅ Verificar espacio disponible en disco
```

### 🔍 Diagnóstico Avanzado

**Para obtener logs detallados:**

1. Usar Opción 4 para analizar video antes de descargar
2. Verificar información de formatos con Opción 8
3. Probar con un video diferente para aislar el problema
4. Cambiar entre motores yt-dlp y pytubefix

## 🛠️ Desarrollo y Contribuciones

### 🏗️ Configuración de Desarrollo

```powershell
# Clonar repositorio
git clone <url-del-repositorio>
cd youtube-downloader

# Configurar entorno de desarrollo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Instalar dependencias de desarrollo (opcional)
pip install black flake8 pytest
```

### 📋 Roadmap de Funcionalidades

**🎯 Próximas versiones:**

- [ ] **GUI opcional**: Interfaz gráfica con tkinter/PyQt
- [ ] **Descarga programada**: Scheduler para descargas automáticas
- [ ] **Subtítulos automáticos**: Descarga de subtítulos en múltiples idiomas
- [ ] **Conversión de formatos**: MP4 a AVI, MKV, etc.
- [ ] **Integración con bases de datos**: SQLite para historial de descargas
- [ ] **API REST**: Endpoint para integración con otras aplicaciones
- [ ] **Docker**: Contenedor para deploy fácil
- [ ] **Configuración personalizada**: Archivo config.json

### 🤝 Cómo Contribuir

**1. Fork y Clone:**

```powershell
git fork <repositorio>
git clone https://github.com/tu-usuario/youtube-downloader.git
```

**2. Crear rama de feature:**

```powershell
git checkout -b feature/nueva-funcionalidad
```

**3. Desarrollo y testing:**

```powershell
# Hacer cambios
python src/main.py  # Probar cambios

# Seguir estándares de código
black src/  # Formateo
flake8 src/  # Linting
```

**4. Commit y Push:**

```powershell
git add .
git commit -m "Add: Nueva funcionalidad XYZ"
git push origin feature/nueva-funcionalidad
```

**5. Pull Request:**

- Descripción clara de cambios
- Screenshots si aplica
- Tests si es posible

### 📝 Estándares de Código

- **PEP 8**: Estilo de código Python
- **Docstrings**: Documentación en funciones importantes
- **Type hints**: Tipos cuando sea posible
- **Error handling**: Manejo robusto de errores
- **Logging**: Usar colorama para salida consistente

## 📄 Licencia y Legal

Este proyecto está bajo la **Licencia MIT**. Ver [LICENSE.md](LICENSE.md) para más detalles.

### ⚖️ Consideraciones Legales

- ✅ **Uso personal**: Descarga para uso personal y educativo
- ⚠️ **Derechos de autor**: Respeta los términos de servicio de YouTube
- 🚫 **Uso comercial**: No redistribuyas contenido con copyright
- 📋 **Responsabilidad**: El usuario es responsable del uso del software

## 🐛 Reporte de Issues

### 📋 Información a Incluir

Al reportar problemas, incluye:

**🔗 URL y detalles:**

- URL completa del video/playlist que falla
- Calidad solicitada
- Motor utilizado (yt-dlp/pytubefix)

**💻 Información del sistema:**

- Sistema operativo (Windows 10/11, macOS, Linux)
- Versión de Python (`python --version`)
- Versiones de dependencias principales

**📝 Logs y errores:**

- Mensaje de error completo
- Output de la consola
- Screenshots si aplica

**🔄 Pasos para reproducir:**

- Secuencia exacta de acciones
- Configuración utilizada
- Comportamiento esperado vs real

### 🏷️ Categorías de Issues

- 🐛 **Bug**: Errores en funcionalidad existente
- ✨ **Feature**: Solicitudes de nuevas funcionalidades
- 📚 **Documentation**: Mejoras en documentación
- 🎨 **UI/UX**: Mejoras en interfaz de usuario
- ⚡ **Performance**: Optimizaciones de rendimiento
- 🔧 **Technical**: Mejoras técnicas internas

## 🔗 Recursos y Enlaces

### 📚 Documentación Técnica

- **[yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)** - Motor principal de descarga
- **[pytubefix Documentation](https://github.com/JuanBindez/pytubefix)** - Motor alternativo
- **[FFmpeg Documentation](https://ffmpeg.org/documentation.html)** - Fusión de streams
- **[colorama Documentation](https://pypi.org/project/colorama/)** - Colores en terminal

### 🎯 Proyectos Relacionados

- **[YouTube-Download Simple](https://github.com/GAROS01/YouTube-Download)** - Versión básica y directa
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Motor de descarga principal
- **[pytubefix](https://github.com/JuanBindez/pytubefix)** - Alternativa moderna a pytube

### 🌐 Comunidad

- **GitHub Issues**: Para reportes y sugerencias
- **GitHub Discussions**: Para preguntas y discusiones
- **Pull Requests**: Para contribuciones de código

## 📊 Estadísticas del Proyecto

| Métrica              | Valor              |
| -------------------- | ------------------ |
| **Líneas de código** | ~800 líneas        |
| **Archivos fuente**  | 4 módulos          |
| **Dependencias**     | 5 packages         |
| **Compatibilidad**   | Python 3.8+        |
| **Plataformas**      | Windows/Mac/Linux  |
| **Calidad máxima**   | 4K + Audio 320kbps |

---

## 🎉 Agradecimientos

**Desarrollado con ❤️ por:**

- **GarosDev** - Desarrollo principal y arquitectura
- **Comunidad Open Source** - Librerías y herramientas
- **Usuarios Beta** - Testing y feedback

### �️ Tecnologías Utilizadas

- **Python 3.8+** - Lenguaje principal
- **yt-dlp** - Motor de descarga avanzado
- **pytubefix** - Motor alternativo confiable
- **colorama** - Interfaz colorida
- **tqdm** - Barras de progreso profesionales
- **FFmpeg** - Procesamiento de video/audio

---

<div align="center">

**🚀 VibeCoding - Desarrollando el futuro, una línea a la vez**

_Si este proyecto te resultó útil, considera darle una ⭐ en GitHub_

[![GitHub Stars](https://img.shields.io/github/stars/GAROS01/youtube-downloader?style=social)](https://github.com/GAROS01/youtube-downloader)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

</div>
