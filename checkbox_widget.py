import streamlit as st

## Checkbox Widget

image_list = ['others/amblem.png', 'others/youtube.png']
caption_list = ['Amblem', 'Youtube']

st.header("Welcome to Streamlit")

checks = st.columns(2)
with checks[0]:
    images = st.checkbox('Do you want to see image?')
with checks[1]:
    codes = st.checkbox('Do you want to see code?')

if images:
    st.image(image=image_list, width=100, caption=caption_list)
if codes:
    st.code("print('Hello Streamlit')")