import streamlit as st
import edge_tts
import asyncio

# Async TTS function
async def generate_tts(text, voice, rate, pitch, filename):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(filename)

# Streamlit UI
st.set_page_config(page_title="Teks ke Suara Bahasa Indonesia", layout="centered")
st.title("🔊 Teks ke Suara (Bahasa Indonesia) - Microsoft Edge TTS")

text_input = st.text_area("📝 Masukkan teks Bahasa Indonesia:", "Halo! Ini adalah contoh suara Bahasa Indonesia menggunakan teknologi Microsoft.")
voice_option = st.selectbox("🗣️ Pilih Suara", ["id-ID-GadisNeural (Perempuan)", "id-ID-ArdiNeural (Laki-laki)"])
rate = st.slider("🎚️ Kecepatan (rate)", -100, 100, 0, step=10)
pitch = st.slider("🎚️ Nada (pitch)", -50, 50, 0, step=5)

voice_map = {
    "id-ID-GadisNeural (Perempuan)": "id-ID-GadisNeural",
    "id-ID-ArdiNeural (Laki-laki)": "id-ID-ArdiNeural"
}

filename = "output.mp3"

if st.button("🔄 Ubah ke Suara"):
    with st.spinner("Membuat suara..."):
        # Format pitch dan rate agar sesuai dengan edge-tts
        formatted_rate = f"{'+' if rate >= 0 else ''}{rate}%"
        formatted_pitch = f"{'+' if pitch >= 0 else ''}{pitch}Hz"

        asyncio.run(generate_tts(
            text=text_input,
            voice=voice_map[voice_option],
            rate=formatted_rate,
            pitch=formatted_pitch,
            filename=filename
        ))

        with open(filename, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.success("✅ Suara berhasil dibuat!")
            st.audio(audio_bytes, format="audio/mp3")
            st.download_button("⬇️ Unduh MP3", audio_bytes, file_name="output.mp3", mime="audio/mp3")
