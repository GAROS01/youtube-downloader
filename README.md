# 🎬 YouTube Downloader

Un descargador de videos de YouTube moderno y fácil de usar, desarrollado en Python con una interfaz de línea de comandos colorida e interactiva.

## ✨ Características

- 🎥 **Descarga videos** en diferentes calidades (1080p, 720p, 480p, 360p, etc.)
- 🎵 **Extrae audio** en formato MP3 de alta calidad (192 kbps)
- 📋 **Información detallada** del video con descripciones extensas
- 🔄 **Dos motores de descarga**: yt-dlp (recomendado) y pytubefix (actualizado)
- 🎨 **Interfaz colorida** con emojis para mejor experiencia de usuario
- 📁 **Directorio personalizable** de descarga
- ✅ **Validación robusta** de URLs de YouTube
- 🛡️ **Manejo robusto de errores** con métodos de respaldo
- 📊 **Análisis detallado** de streams disponibles
- 🔍 **Vista previa** de descripciones con opción de ver contenido completo

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
5. **Cambiar directorio de descarga** - Personaliza la carpeta destino
6. **Ver calidades disponibles** - Muestra todas las opciones de calidad
7. **Salir** - Cierra la aplicación

### Ejemplo de uso

```
🎬 DESCARGADOR DE VIDEOS DE YOUTUBE
==================================================
1. Descargar video (yt-dlp)
2. Descargar video (pytubefix)
3. Descargar solo audio (MP3)
4. Obtener información del video
5. Cambiar directorio de descarga
6. Ver calidades disponibles
0. Salir
==================================================

Selecciona una opción (0-6): 1
📎 Ingresa la URL del video: https://www.youtube.com/watch?v=ejemplo
Calidades disponibles: best, 1080p, 720p, 480p, 360p, 240p, worst
🎥 Calidad [best]: 1080p
🔄 Descargando video en calidad: 1080p...
✅ Descarga completada exitosamente
📁 Guardado en: downloads
```

### Información detallada de videos

Cuando selecciones la opción 4, obtendrás información completa como:

```
📋 INFORMACIÓN DEL VIDEO (PyTubeFix)
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
    • 720p - 245.8 MB
    • 480p - 156.2 MB
    • 360p - 98.7 MB

📝 Descripción:
  En este tutorial completo aprenderás Python desde cero hasta nivel
  avanzado. Cubrimos todos los conceptos fundamentales incluyendo...

¿Mostrar descripción completa? (s/n):
```

## 📦 Dependencias

- **yt-dlp** ≥ 2023.7.6 - Motor principal de descarga, más estable
- **pytubefix** ≥ 6.10.2 - Motor alternativo actualizado (reemplaza pytube)
- **requests** ≥ 2.31.0 - Peticiones HTTP
- **colorama** ≥ 0.4.6 - Colores en terminal
- **tqdm** ≥ 4.65.0 - Barras de progreso

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

- **Streams progresivos**: Video y audio en un solo archivo
- **Streams adaptativos**: Video y audio por separado para mejor calidad
- **Información de tamaños**: Muestra el tamaño estimado antes de descargar
- **Fallback inteligente**: Si un método falla, automáticamente usa el alternativo
- **Descripciones interactivas**: Vista previa con opción de ver contenido completo

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

### pytubefix (Alternativo)

- ✅ Más rápido para información básica
- ✅ Interfaz más simple
- ✅ Mejor para análisis de streams
- ✅ Actualizado regularmente (2024)
- ✅ Reemplaza a pytube obsoleto

## 🛠️ Desarrollo

### Instalación para desarrollo

```bash
pip install -e ".[dev]"
```

### Estructura de clases

- **Downloader**: Clase principal para gestión de descargas con ambos métodos
- **VideoInfo**: Clase especializada para obtener información de videos
- **validate_url()**: Función para validar URLs de YouTube
- **format_filename()**: Función para limpiar nombres de archivo

### Arquitectura

- **Separación de responsabilidades**: Cada clase tiene una función específica
- **Manejo de errores robusto**: Múltiples métodos de respaldo
- **Interfaz consistente**: API unificada para ambos motores de descarga
- **Escalabilidad**: Fácil agregar nuevos métodos de descarga

## 🎨 Interfaz de Usuario

- **Colores dinámicos**: Diferentes colores para diferentes tipos de información
- **Emojis descriptivos**: Fácil identificación visual de opciones
- **Mensajes informativos**: Retroalimentación clara del progreso
- **Interactividad**: Opciones para personalizar la experiencia

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

## 📈 Changelog

### v0.1.0 (Actual)

- ✅ Implementación de pytubefix en lugar de pytube
- ✅ Clase VideoInfo separada para mejor organización
- ✅ Información detallada de streams disponibles
- ✅ Descripciones interactivas extensas
- ✅ Soporte para 1080p
- ✅ Mejor manejo de errores con fallback automático
- ✅ Interfaz mejorada con más opciones
- ✅ Documentación completa

## 🔮 Próximas Características

- 🔄 Descarga de playlists completas
- 📊 Progreso visual con barras de descarga
- 🎵 Más formatos de audio (FLAC, AAC)
- 📱 Interfaz gráfica opcional
- 🌐 Soporte para más plataformas de video

---

**Desarrollado por GarosDev** 🚀

_Última actualización: Diciembre 2024_
