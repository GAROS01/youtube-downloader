import re
from urllib.parse import urlparse

def validate_url(url):
    """Valida si la URL es de YouTube (video o playlist) y está bien formada"""
    if not url:
        return False
    
    # Patrones de URLs válidas de YouTube (videos y playlists)
    youtube_patterns = [
        # Videos individuales
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+',
        r'(?:https?://)?(?:www\.)?youtu\.be/[\w-]+',
        r'(?:https?://)?(?:www\.)?youtube\.com/embed/[\w-]+',
        r'(?:https?://)?(?:www\.)?youtube\.com/v/[\w-]+',
        # Playlists
        r'(?:https?://)?(?:www\.)?youtube\.com/playlist\?list=[\w-]+',
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+&list=[\w-]+',
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?list=[\w-]+',
    ]
    
    for pattern in youtube_patterns:
        if re.match(pattern, url):
            return True
    
    return False

def format_filename(title):
    """Limpia el título del video para usarlo como nombre de archivo"""
    # Remover caracteres no válidos para nombres de archivo
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '')
    
    # Limitar longitud
    if len(title) > 100:
        title = title[:100]
    
    return title.strip()