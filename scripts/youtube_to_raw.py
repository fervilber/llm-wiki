import sys
import re
import os
import urllib.request
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_id(url):
    # Extraer el ID del video de varios formatos de URLs de YouTube
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if match:
        return match.group(1)
    
    # Manejar youtu.be
    match = re.search(r"youtu\.be\/([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

import urllib.request
import ssl

def get_video_title(url):
    try:
        # Bypass SSL verification for macOS certificate issues
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=context).read().decode('utf-8')
        match = re.search(r'<title>(.*?)</title>', html)
        if match:
            title = match.group(1)
            title = title.replace(" - YouTube", "")
            # Limpiar el título para que sea un nombre de archivo válido
            title = re.sub(r'[^\w\s-]', '', title).strip()
            title = re.sub(r'[-\s]+', '_', title)
            return title
    except Exception as e:
        print(f"⚠️ No se pudo obtener el título automáticamente: {e}")
    return "transcripcion"

def fetch_transcript(url, output_filename=None):
    video_id = get_video_id(url)
    if not video_id:
        print(f"Error: No se pudo extraer el ID del video de la URL: {url}")
        return
    
    if not output_filename:
        print("Obteniendo título del vídeo...")
        output_filename = get_video_title(url)
        print(f"Título detectado: {output_filename}")
        
    filepath = f"raw/{output_filename}.md"
    if os.path.exists(filepath):
        print(f"⚠️ Aviso: El archivo '{filepath}' ya existe. Descarga cancelada para evitar duplicados.")
        return
    
    try:
        # Obtener lista de transcripciones disponibles
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        
        try:
            # Intentar obtener en español o inglés
            transcript = transcript_list.find_transcript(['es', 'en'])
        except:
            # Si no, buscar la primera disponible
            transcript = transcript_list.find_generated_transcript(['es', 'en'])

        # Descargar y formatear la transcripción
        transcript_data = transcript.fetch()
        formatter = TextFormatter()
        text_formatted = formatter.format_transcript(transcript_data)
        
        # Asegurar que el directorio raw existe
        os.makedirs("raw", exist_ok=True)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"title: \"Transcripción: {output_filename}\"\n")
            f.write(f"source: \"{url}\"\n")
            f.write("tags: [youtube, transcripcion]\n")
            f.write("---\n\n")
            f.write(f"# Transcripción de YouTube\n\n")
            f.write(f"**URL**: {url}\n\n")
            f.write("---\n\n")
            f.write(text_formatted)
            
        print(f"✅ Éxito: Transcripción guardada correctamente en '{filepath}'")
        
    except Exception as e:
        print(f"❌ Error al obtener transcripción: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python youtube_to_raw.py <URL_DE_YOUTUBE> [NOMBRE_ARCHIVO_DESTINO]")
        print("Ejemplo 1 (título automático): python youtube_to_raw.py 'https://youtu.be/...'")
        print("Ejemplo 2 (nombre manual): python youtube_to_raw.py 'https://youtu.be/...' 'video_economia'")
        sys.exit(1)
        
    url = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) >= 3 else None
    fetch_transcript(url, filename)
