import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer 
import utils.backend_utils as backend

dir_path = os.getcwd()

@st.cache_data
def create_sidebar(dir_path=dir_path):

    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Osher's Resume App</h1>", unsafe_allow_html=True)
    st.sidebar.image(fr'{dir_path}\resume\self.jpeg')
    st.sidebar.markdown("## __About Osher__")


    about = "I am a data scientist with a passion for transforming dataframes into actionable insights. \
    With a background in computer science and statistics, I specialize in building robust machine learning algorithms and conducting statistical analysis of any dataset that comes my way. \
    My expertise in Python, SQL and cloud-based architectures have allowed me to develop scalable tools that provide unique solutions."

    st.sidebar.write(about)

def resume_view_and_download(resume_pdf_path = backend.resume_pdf_path, resume_download_name=backend.resume_name):
    with st.expander('View Resume PDF'):
        pdf_viewer(resume_pdf_path)



    st.download_button("Download Resume", data=backend.pdf_reader(resume_pdf_path), file_name=resume_download_name)