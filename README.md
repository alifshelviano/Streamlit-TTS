# Streamlit TTS (Text-to-Speech) Bahasa Indonesia

A simple web application to convert Indonesian text to speech using Google gTTS and Microsoft Edge TTS, built with Streamlit.

## Features

- Convert Indonesian text to speech (Bahasa Indonesia)
- Choose between Google gTTS or Microsoft Edge TTS voices
- Select voice type (male/female), adjust speed and pitch (Edge TTS)
- Play and download generated MP3 audio

## Installation

1. Clone this repository or download the source code.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run either app with Streamlit:

- **Google TTS:**
  ```
  streamlit run googlevc.py
  ```

- **Microsoft Edge TTS:**
  ```
  streamlit run edgevc.py
  ```

## Files

- `googlevc.py` — Streamlit app using Google gTTS
- `edgevc.py` — Streamlit app using Microsoft Edge TTS
- `requirements.txt` — Python dependencies

## Live

- Google TTS

https://edgestexttovc.streamlit.app/

- Edges TTS

https://gtxttovoice.streamlit.app/

## License

For educational and personal
