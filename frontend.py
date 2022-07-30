from download import *
import streamlit as st

st.title('Helmet Detector')

url = st.text_input("Enter URL")

# url = "https://drive.google.com/file/d/11q7_j10LGkg0QOlTNur5yl2zIB7x_mV_/view?usp=sharing"
if st.button("Find faults"):
    faults = find_faults(url)
    st.write(f"Found {len(faults)}!")
    for fault in faults:
        st.image(fault)
