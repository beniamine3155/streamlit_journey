import streamlit as st

## Image, Audio and Video

st.image('others/tennis.jpg', caption="This is tennis image", width=400)

## Audio start will be after 50 seconds
st.audio('others/audio.oga', start_time=50)

st.video('others/video.mp4')