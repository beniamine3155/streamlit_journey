import streamlit as st

## Input and Button

car_types = ['toyota', 'ford', 'fiat', 'bmw']

car = st.text_input("Type a car")
button = st.button('Check Availability')

if button == True:
    have_it = car.lower() in car_types
    if have_it:
        st.write("We have that car")
    else:
        st.write("We don't have that car")