import streamlit as st

## Toggle Widget
st.header("Welcome to Streamlit Code!")

toggles = st.columns(3)
with toggles[0]:
    toggle_image = st.toggle('Enable Image')

with toggles[1]:
    toggle_audio = st.toggle('Enable Audio')

with toggles[2]:
    toggle_video = st.toggle('Enable Video')


if toggle_image:
    st.image('others/youtube.png', width=200)

if toggle_audio:
    st.audio('others/audio.oga')

if toggle_video:
    st.video('others/video.mp4')

