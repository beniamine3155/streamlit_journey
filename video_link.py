import streamlit as st

## Image list and video link

image_list = ['others/amblem.png', 'others/youtube.png']
caption_list = ['Amblem', 'YouTube']

st.header("Welcome to Streamlit")
st.image(image=image_list, width=100, caption=caption_list)

st.link_button('Go to Streamlit Tutorial', 'https://www.youtube.com/watch?v=D0D4Pa22iG0&ab_channel=pixegami')



