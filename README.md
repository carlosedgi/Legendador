
# 🧠 Whisper Video Subtitles Generator

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![Whisper](https://img.shields.io/badge/Powered%20by-Whisper-brightgreen)](https://github.com/openai/whisper)  
[![FFmpeg](https://img.shields.io/badge/Tool-FFmpeg-green)](https://ffmpeg.org/)  
[![Twitter](https://img.shields.io/badge/X-Sentinela%20Carioca-1DA1F2?logo=twitter)](https://x.com/SentinelaCarioca)

Este repositório contém um script Python que converte vídeos em texto legendado automaticamente, utilizando a inteligência artificial do modelo Whisper da OpenAI. Ele permite **transcrição de áudio**, **tradução para outro idioma** e **geração de legendas no formato `.srt`**.

---

## 📌 Funcionalidades

- 🎥 Converte vídeos para áudio com **FFmpeg**
- 🧠 Transcreve com **Whisper**
- 🌍 Tradução automática via **Google Translate** com `deep-translator`
- 📝 Geração de legendas `.srt` sincronizadas
- 🔁 Suporte a múltiplos idiomas (original e traduzido)
- 💬 Ideal para vídeos educativos, entrevistas, podcasts, etc.

---

## ⚙️ Requisitos

### Dependências do sistema

- [FFmpeg](https://ffmpeg.org/download.html) instalado e acessível via terminal (verifique com `ffmpeg -version`)

### Bibliotecas Python

Instale com:

```bash
pip install openai-whisper tqdm deep-translator
```

Recomenda-se uso de ambiente virtual (`venv` ou `conda`).

---

## 🚀 Como usar

1. Clone este repositório
2. Execute o script:

```bash
python video_legenda.py
```

3. Siga as instruções interativas:

```plaintext
Digite o caminho do vídeo: exemplo.mp4
Idioma do áudio (ex: en, pt, es) [padrão: pt]: en
Idioma para tradução (ex: en, pt, es) [padrão: pt]: pt
```

4. O arquivo `.srt` será salvo na pasta `legendas`.

---

## 🧩 Exemplo

Dado um vídeo em inglês `entrevista.mp4`, com a entrada:

```plaintext
Idioma do áudio: en
Idioma para tradução: pt
```

Será gerado:

```bash
legendas/entrevista.srt
```

---

## 🧠 Sobre o projeto

Este projeto foi desenvolvido por **Carlos Eduardo d’Ávila Garcia Isaias** com apoio do ChatGPT, e faz parte da iniciativa de **compartilhamento de conhecimento descentralizado** pelo perfil [@SentinelaCarioca](https://x.com/SentinelaCarioca) no X (Twitter).

> 🌍 “O conhecimento é mais poderoso quando distribuído.”

---

## 🔗 Referências

- [Whisper – OpenAI](https://github.com/openai/whisper)
- [FFmpeg – Site oficial](https://ffmpeg.org/)
- [deep-translator – PyPI](https://pypi.org/project/deep-translator/)
- [Python tqdm – Barra de progresso](https://github.com/tqdm/tqdm)

---

## 📜 Licença

Distribuído sob a [Licença MIT](LICENSE).  
Use, modifique e compartilhe livremente ✊
