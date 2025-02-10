import streamlit as st
import gdown 

@st.cache_data
def download_google_doc_file(url, output_file_name):

    gdown.download(url, output_file_name, quiet=False, fuzzy=True)
    return "File has been downloaded"