# 🎬 YouTube Downloader

Un descargador de videos de YouTube moderno y fácil de usar, desarrollado en Python con una interfaz de línea de comandos colorida e interactiva.

## ✨ Características

- 🎥 **Descarga videos** en diferentes calidades (1080p, 720p, 480p, 360p, etc.)
- 🎵 **Extrae audio** en formato MP3 de alta calidad (192 kbps)
- 📊 **Barras de progreso avanzadas** con velocidad de descarga y tiempo estimado
- 📋 **Información detallada** del video con descripciones extensas
- 🔄 **Dos motores de descarga**: yt-dlp (recomendado) y pytubefix (actualizado)
- 📦 **Descarga múltiple** con progreso individual y general
- 🎨 **Interfaz colorida** con emojis para mejor experiencia de usuario
- 📁 **Directorio personalizable** de descarga
- ✅ **Validación robusta** de URLs de YouTube
- 🛡️ **Manejo robusto de errores** con métodos de respaldo
- 🔍 **Análisis detallado** de streams disponibles con progreso visual
- 💡 **Vista previa** de descripciones con opción de ver contenido completo

## 📁 Estructura del Proyecto

```
youtube-downloader/
├── src/
│   ├── main.py              # Punto de entrada con menú interactivo
│   ├── Class/
│   │   ├── downloader.py    # Clase principal para descargas
│   │   └── info.py          # Clase para obtener información de videos
│   └── utils/
│       └── __init__.py      # Funciones utilitarias (validación, formato)
├── requirements.txt         # Dependencias del proyecto
├── setup.py                # Configuración del paquete
├── LICENSE                 # Licencia MIT
├── .gitignore             # Archivos ignorados por Git
├── .venv/                 # Entorno virtual (creado localmente)
└── README.md              # Documentación del proyecto
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

1. **Descargar video (yt-dlp)** - Método recomendado, más estable y versátil
2. **Descargar video (pytubefix)** - Método alternativo actualizado y rápido
3. **Descargar solo audio (MP3)** - Extrae únicamente el audio en alta calidad
4. **Obtener información del video** - Muestra detalles completos sin descargar
5. **Descargar múltiples videos** - Descarga varios videos con progreso general
6. **Cambiar directorio de descarga** - Personaliza la carpeta destino
7. **Ver calidades disponibles** - Muestra todas las opciones de calidad
8. **Salir** - Cierra la aplicación

### Ejemplo de uso con barra de progreso

```
🎬 DESCARGADOR DE VIDEOS DE YOUTUBE
=======================================================
1. Descargar video (yt-dlp) 📥
2. Descargar video (pytubefix) 🚀
3. Descargar solo audio (MP3) 🎵
4. Obtener información del video 📊
5. Descargar múltiples videos 📦
6. Cambiar directorio de descarga 📁
7. Ver calidades disponibles 🎥
0. Salir 👋
=======================================================

Selecciona una opción (0-7): 1
📎 Ingresa la URL del video: https://www.youtube.com/watch?v=ejemplo
🎥 Calidades disponibles: best, 1080p, 720p, 480p, 360p, 240p, worst
🎬 Calidad [best]: 1080p

🎬 Descargando video en calidad: 1080p...
📥 Descargando ████████████████████████████████████████ 100%  245.8M/245.8M [2.4MB/s]
✅ Descarga completada: Tutorial completo de Python 2024.mp4
🎉 Descarga completada exitosamente
📁 Guardado en: downloads
```

### Información detallada de videos con progreso

```
📎 Ingresa la URL del video: https://www.youtube.com/watch?v=ejemplo

🔍 Analizando video ██████████████████████████████████████████ 100%
🔗 Conectando → 📊 Obteniendo datos → 🎥 Analizando streams → ✅ Completado

============================================================
📋 INFORMACIÓN DEL VIDEO
============================================================
📹 Título: Tutorial completo de Python 2024
👤 Autor: Canal de Programación
📺 Canal: https://www.youtube.com/channel/ejemplo
⏱️ Duración: 15:30
👁️ Vistas: 1,234,567
📅 Fecha de publicación: 15/12/2024
🎥 Calidades disponibles: 1080p, 720p, 480p, 360p

📊 Información de streams disponibles:
  🎬 Videos progresivos (video + audio):
    • 720p - 245.8 MB - mp4
    • 480p - 156.2 MB - mp4
    • 360p - 98.7 MB - mp4

  🎥 Videos adaptativos (solo video):
    • 1080p - 312.5 MB - mp4
    • 720p - 187.3 MB - mp4

  🎵 Audio disponible:
    • 192 kbps - 28.4 MB - mp4a
    • 128 kbps - 18.9 MB - mp4a
```

### Descarga múltiple con progreso

```
Selecciona una opción (0-7): 5
📝 Ingresa las URLs (presiona Enter sin texto para terminar):
URL 1: https://www.youtube.com/watch?v=video1
URL 2: https://www.youtube.com/watch?v=video2
URL 3: https://www.youtube.com/watch?v=video3
URL 4: 

🎥 Calidades disponibles: best, 1080p, 720p, 480p, 360p, 240p, worst
🎬 Calidad para todos [best]: 720p

📦 Descargando 3 videos...
🎬 Videos ████████████████████████████████████████ 3/3 videos

📹 Descargando video 1/3
📥 Descargando ████████████████████████████████████████ 100%  156.2M/156.2M [1.8MB/s]
✅ Descarga completada: Video Tutorial 1.mp4

📹 Descargando video 2/3
📥 Descargando ████████████████████████████████████████ 100%  203.5M/203.5M [2.1MB/s]
✅ Descarga completada: Video Tutorial 2.mp4

📹 Descargando video 3/3
📥 Descargando ████████████████████████████████████████ 100%  189.7M/189.7M [1.9MB/s]
✅ Descarga completada: Video Tutorial 3.mp4

🎉 Descarga completada: 3/3 videos exitosos
```

## 📦 Dependencias

- **yt-dlp** - Motor principal de descarga, más estable
- **pytubefix** - Motor alternativo actualizado (reemplaza pytube)
- **requests** - Peticiones HTTP
- **colorama** - Colores en terminal
- **tqdm** - Barras de progreso avanzadas con velocidad y tiempo estimado

## 🎨 Características Visuales

### Barras de Progreso Avanzadas

- **Velocidad de descarga**: Muestra MB/s en tiempo real
- **Progreso visual**: Barras coloridas con porcentajes
- **Tiempo estimado**: Cálculo automático del tiempo restante
- **Tamaño del archivo**: Descargado/Total en formato legible
- **Múltiples procesos**: Progreso individual y general para descargas múltiples

### Análisis de Video con Progreso

```
🔍 Analizando video ██████████████████████████████████████████ 100%
🔗 Conectando (20%) → 📊 Obteniendo datos (50%) → 🎥 Analizando streams (75%) → ✅ Completado (100%)
```

### Descarga con Información Detallada

```
📥 Descargando ████████████████████████████████████████ 100%  245.8M/245.8M [2.4MB/s]
▶️ Tiempo transcurrido: 02:15  |  ⏱️ Tiempo restante: 00:00
```

## 🔧 Funcionalidades Técnicas

### Validación de URLs

El programa acepta los siguientes formatos de URL de YouTube:

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `https://www.youtube.com/v/VIDEO_ID`

### Formatos de Descarga

- **Video**: MP4 en diferentes resoluciones (1080p, 720p, 480p, 360p, 240p)
- **Audio**: MP3 con calidad de 192 kbps
- **Calidades disponibles**: best, 1080p, 720p, 480p, 360p, 240p, worst

### Características Avanzadas

- **Progreso en tiempo real**: Barras de progreso con `tqdm` para todas las operaciones
- **Streams progresivos**: Video y audio en un solo archivo
- **Streams adaptativos**: Video y audio por separado para mejor calidad
- **Información de tamaños**: Muestra el tamaño estimado antes de descargar
- **Fallback inteligente**: Si un método falla, automáticamente usa el alternativo
- **Descarga múltiple**: Procesa varios videos con progreso general
- **Callbacks de progreso**: Hooks personalizados para cada motor de descarga

### Gestión de Archivos

- Limpieza automática de nombres de archivo
- Creación automática de directorio de descarga
- Validación de caracteres especiales
- Organización por carpetas

## 🔄 Métodos de Descarga

### yt-dlp (Recomendado)

- ✅ Más estable y confiable
- ✅ Mejor manejo de restricciones
- ✅ Actualizaciones frecuentes
- ✅ Soporte para más formatos
- ✅ Mejor calidad de video
- ✅ Barras de progreso nativas integradas

### pytubefix (Alternativo)

- ✅ Más rápido para información básica
- ✅ Interfaz más simple
- ✅ Mejor para análisis de streams
- ✅ Actualizado regularmente (2024)
- ✅ Reemplaza a pytube obsoleto
- ✅ Callbacks personalizados de progreso

## 🛠️ Desarrollo

### Instalación para desarrollo

```bash
pip install -e ".[dev]"
```

### Estructura de clases

- **Downloader**: Clase principal para gestión de descargas con barras de progreso
- **VideoInfo**: Clase especializada para obtener información con progreso visual
- **validate_url()**: Función para validar URLs de YouTube
- **format_filename()**: Función para limpiar nombres de archivo
- **progress_hook()**: Callback para barras de progreso de yt-dlp
- **progress_function_pytube()**: Callback para barras de progreso de pytubefix

### Arquitectura

- **Separación de responsabilidades**: Cada clase tiene una función específica
- **Manejo de errores robusto**: Múltiples métodos de respaldo
- **Interfaz consistente**: API unificada para ambos motores de descarga
- **Escalabilidad**: Fácil agregar nuevos métodos de descarga
- **Progreso visual**: Integración completa de `tqdm` en todas las operaciones

## 🎨 Interfaz de Usuario

- **Colores dinámicos**: Diferentes colores para diferentes tipos de información
- **Emojis descriptivos**: Fácil identificación visual de opciones
- **Barras de progreso**: Visualización en tiempo real del progreso
- **Mensajes informativos**: Retroalimentación clara del progreso
- **Interactividad**: Opciones para personalizar la experiencia
- **Progreso detallado**: Múltiples fases del proceso claramente mostradas

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
- Método de descarga utilizado (yt-dlp o pytubefix)
- Información de la barra de progreso (si se detuvo)

## 📈 Changelog

### v0.2.0 (Actual)

- ✅ **Barras de progreso avanzadas** con `tqdm` integrado
- ✅ **Velocidad de descarga** mostrada en tiempo real
- ✅ **Progreso para análisis** de información de video
- ✅ **Descarga múltiple** con progreso general e individual
- ✅ **Callbacks personalizados** para ambos motores
- ✅ **Interfaz mejorada** con mejor feedback visual
- ✅ **Tiempo estimado** y estadísticas de descarga

### v0.1.0

- ✅ Implementación de pytubefix en lugar de pytube
- ✅ Clase VideoInfo separada para mejor organización
- ✅ Información detallada de streams disponibles
- ✅ Descripciones interactivas extensas
- ✅ Soporte para 1080p
- ✅ Mejor manejo de errores con fallback automático
- ✅ Interfaz mejorada con más opciones
- ✅ Documentación completa

## 🔮 Próximas Características

- 🔄 Descarga de playlists completas con progreso
- 🎵 Más formatos de audio (FLAC, AAC)
- 📱 Interfaz gráfica con barras de progreso
- 🌐 Soporte para más plataformas de video
- ⚡ Descarga paralela con múltiples hilos
- 📊 Estadísticas de descarga y reportes

---

**Desarrollado por GarosDev** 🚀

_Última actualización: Diciembre 2024 - v0.2.0 con barras de progreso avanzadas_
