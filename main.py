import pandas as pd 
import streamlit as st
from PIL import Image




profile_picture = Image.open('self.jpeg')

st.sidebar.image(profile_picture)
st.sidebar.write("Welcome to my resume website!")



