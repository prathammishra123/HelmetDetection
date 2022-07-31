# This file creates front end for me using a library in python called streamlit
from final import *
import streamlit as st
# final is a file that has a function find_faults that takes a url download the video and find faults in it returning an array of images .
st.title('Helmet Detector')
url = st.text_input("Enter URL")
# sample url
# url = "https://drive.google.com/file/d/11q7_j10LGkg0QOlTNur5yl2zIB7x_mV_/view?usp=sharing"
if st.button("Find faults"):
    faults = find_faults(url)
    st.write(f"Found {len(faults)}!")
    for fault in faults:
        st.image(fault)
