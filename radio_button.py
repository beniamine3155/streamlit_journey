import streamlit as st

## radio button widget

st.header("Choose Your Course!!!")

radio_button = st.radio('Choose your course',
                        ["HTML | CSS :rainbow:",
                         "JavaScript :large_blue_circle:",
                         "Python :large_green_circle:"
                         ],
                         index=None
                        )

if radio_button == "HTML | CSS :rainbow:":
    st.write("You Selected HTML | CSS")
elif radio_button == "JavaScript :large_blue_circle:":
    st.write("You Selected JavaScript")
elif radio_button == "Python :large_green_circle:":
    st.write("You Selected Python")