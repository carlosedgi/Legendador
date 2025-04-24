import os
import subprocess
import whisper
from datetime import timedelta
from tqdm import tqdm
from deep_translator import GoogleTranslator
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def convert_video_to_audio(video_path, audio_path):
    """Converte um arquivo de vídeo para áudio usando FFmpeg."""
    command = ["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", "-y", audio_path]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def format_timestamp(seconds):
    """Converte segundos para o formato hh:mm:ss,SSS."""
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{str(timedelta(seconds=int(seconds)))}.{milliseconds:03d}".replace(".", ",")

def transcribe_audio(audio_path, source_lang):
    """Transcreve o áudio usando Whisper com barra de progresso."""
    model = whisper.load_model("medium")  # Pode mudar para "small", "large", etc.
    result = model.transcribe(audio_path, language=source_lang)
    
    segments = result["segments"]
    total_segments = len(segments)
    
    transcription = []
    print("Processando transcrição...")
    for segment in tqdm(segments, desc="Transcrevendo", unit=" segmento"):
        transcription.append(segment)
    
    return transcription, result["text"]

def translate_text(text, target_lang):
    """Traduz o texto para o idioma desejado usando Google Translate."""
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

def translate_transcription(transcription, target_lang):
    """Traduz cada segmento da transcrição."""
    print("Traduzindo transcrição...")
    for segment in tqdm(transcription, desc="Traduzindo", unit=" segmento"):
        segment["text"] = translate_text(segment["text"], target_lang)
    return transcription

def format_srt(transcription, output_srt_path):
    """Formata a transcrição no padrão SRT e salva o arquivo."""
    with open(output_srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(transcription, start=1):
            start_time = format_timestamp(segment["start"])
            end_time = format_timestamp(segment["end"])
            
            f.write(f"{i}\n{start_time} --> {end_time}\n{segment['text']}\n\n")

def process_video(video_path, source_lang="pt", target_lang="pt"):
    """Processa o vídeo, gerando a legenda traduzida no formato SRT."""
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = f"{base_name}.mp3"
    srt_path = os.path.join("legendas", f"{base_name}.srt")
    
    os.makedirs("legendas", exist_ok=True)
    
    print("Convertendo vídeo para áudio...")
    convert_video_to_audio(video_path, audio_path)
    
    print("Transcrevendo áudio...")
    transcription, _ = transcribe_audio(audio_path, source_lang)
    
    if source_lang != target_lang:
        print("Traduzindo transcrição...")
        transcription = translate_transcription(transcription, target_lang)
    
    print("Gerando arquivo SRT...")
    format_srt(transcription, srt_path)
    
    print(f"Legenda salva em {srt_path}")
    os.remove(audio_path)  # Remove o arquivo de áudio temporário

# Exemplo de uso
def main():
    video_path = input("Digite o caminho do vídeo: ")
    source_lang = input("Idioma do áudio (ex: en, pt, es) [padrão: pt]: ") or "pt"
    target_lang = input("Idioma para tradução (ex: en, pt, es) [padrão: pt]: ") or "pt"
    process_video(video_path, source_lang, target_lang)

if __name__ == "__main__":
    main()
