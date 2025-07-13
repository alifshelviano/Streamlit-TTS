import streamlit as st
import edge_tts
import asyncio
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load Gemini API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Async TTS function
async def generate_tts(text, voice, rate, pitch, filename):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(filename)

# Extract text from uploaded file
def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        import PyPDF2
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])
    elif file.name.endswith(".docx"):
        import docx
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""

# Generate poem from text using Gemini
def generate_poem_from_text(text):
    prompt = f"Buatkan puisi dalam Bahasa Indonesia yang terinspirasi dari konten berikut:\n\n{text}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Puisi AI ke Suara", layout="centered")
st.title("🎙️ Puisi dari File ke Suara (Bahasa Indonesia)")

uploaded_file = st.file_uploader("📂 Unggah file (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])
voice_option = st.selectbox("🗣️ Pilih Suara", ["id-ID-GadisNeural (Perempuan)", "id-ID-ArdiNeural (Laki-laki)"])
rate = st.slider("🎚️ Kecepatan (rate)", -100, 100, 0, step=10)
pitch = st.slider("🎚️ Nada (pitch)", -50, 50, 0, step=5)

voice_map = {
    "id-ID-GadisNeural (Perempuan)": "id-ID-GadisNeural",
    "id-ID-ArdiNeural (Laki-laki)": "id-ID-ArdiNeural"
}

if uploaded_file and st.button("🔄 Buat Puisi dan Ubah ke Suara"):
    with st.spinner("📖 Membaca file dan membuat puisi..."):
        text = extract_text(uploaded_file)
        if not text.strip():
            st.error("⚠️ Gagal membaca isi file.")
        else:
            poem = generate_poem_from_text(text)
            st.subheader("📜 Puisi yang Dihasilkan:")
            st.text_area("Hasil Puisi", poem, height=250)

            formatted_rate = f"{'+' if rate >= 0 else ''}{rate}%"
            formatted_pitch = f"{'+' if pitch >= 0 else ''}{pitch}Hz"
            filename = "puisi_output.mp3"

            asyncio.run(generate_tts(
                text=poem,
                voice=voice_map[voice_option],
                rate=formatted_rate,
                pitch=formatted_pitch,
                filename=filename
            ))

            with open(filename, "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.success("✅ Suara puisi berhasil dibuat!")
                st.audio(audio_bytes, format="audio/mp3")
                st.download_button("⬇️ Unduh MP3", audio_bytes, file_name=filename, mime="audio/mp3")
