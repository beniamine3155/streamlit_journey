import streamlit as st

## Set image file name and download

st.image('others/tennis.jpg', caption="This is tennis image")
file_name = st.text_input("Enter the file name: ")
st.write(file_name)

with open('others/tennis.jpg', "rb") as file:
    btn = st.download_button(
        label="Download Image",
        data=file,
        file_name=file_name,
        mime="image/png"
    )
