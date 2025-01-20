import streamlit as st
import main
from main import get_apod

get_apod()

st.set_page_config(layout = "wide")

col1= st.columns(1)

with col1:
    st.image("image.jpg")




