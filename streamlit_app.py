import streamlit as st
import whisper

st.title("Transcription")

audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if st.button("Transcribe Audio"):
    if audio_file is not None:
        st.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.success("Transcription Complete")
        st.markdown(transcription["text"])
    else:
        st.error("Please upload an audio file")


st.header("Play Original Audio File")
st.audio(audio_file)
