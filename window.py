import streamlit as st

st.title("Przetwarzanie języka naturalnego - NLP")
st.write("Aplikacja do streszczania tekstu przy uzyciu NLP")


file = st.file_uploader("Wybierz plik audio", type=["mp3", "wav"])
if file is not None:
    st.audio(file, format='mp3/wav')
    st.write("Plik audio został wgrany pomyślnie!")





