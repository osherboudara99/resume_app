import pandas as pd 
import streamlit as st
from pathlib import Path
import os 
import utils.backend_utils as backend, utils.frontend_utils as frontend


frontend.create_sidebar()

backend.download_multiple_google_doc_files()

resume_markdown = backend.read_and_correct_resume_markdown()
st.markdown(resume_markdown, unsafe_allow_html=True)

st.divider()


frontend.resume_view_and_download()



