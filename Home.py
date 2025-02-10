import pandas as pd 
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

from resume_pdf_downloader import  download_google_doc_file


# resume = 

# profile_picture = Image.open('self.jpeg')
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Osher's Resume App</h1>", unsafe_allow_html=True)
st.sidebar.image('self.jpeg')
st.sidebar.markdown("## __About Osher__")
st.markdown("<h1 style='text-align: center; color: white;'>Osher's Resume</h1>", unsafe_allow_html=True)


about = "I am a data scientist with a passion for transforming dataframes into actionable insights. \
With a background in computer science and statistics, I specialize in building robust machine learning algorithms and conducting statistical analysis of any dataset that comes my way. \
My expertise in Python, SQL and cloud-based architectures have allowed me to develop scalable tools that provide unique solutions."

st.sidebar.write(about)

resume_url = "https://docs.google.com/document/d/1gql8n7U8WHkdLEu6R6wFI41tLWpnY5QiKQCwdsKMlQA/export?format=pdf"

resume_name = 'osher_resume.pdf'

download_google_doc_file(resume_url, resume_name)

with st.expander('View Resume PDF'):
    pdf_viewer(resume_name)

@st.cache_data
def resume_reader(resume_name=resume_name):
    with open(resume_name, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    return PDFbyte

st.download_button("Download Resume", data=resume_reader(), file_name='osher_boudara_resume.pdf')


