import streamlit as st
from gtts import gTTS
import os

st.title("🔊 Teks ke Suara (Bahasa Indonesia) dengan gTTS")

# Input teks
teks = st.text_area("Masukkan teks dalam Bahasa Indonesia", "Halo! Ini contoh suara Google Text to Speech dalam Bahasa Indonesia.")

if st.button("Ubah ke Suara"):
    # Buat audio dari teks
    tts = gTTS(text=teks, lang='id')
    tts.save("output.mp3")

    # Tampilkan audio player
    audio_file = open("output.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

    # Unduh file
    st.download_button(label="🎧 Unduh Suara", data=audio_bytes, file_name="output.mp3", mime="audio/mp3")
