import streamlit as st
import utils.backend_utils as backend, utils.frontend_utils as frontend

frontend.create_sidebar()

st.markdown("<h1 style='text-align: center; color: white;'>Osher's Resume</h1>", unsafe_allow_html=True)


backend.download_multiple_google_doc_files()

resume_markdown = backend.read_and_correct_resume_markdown()
st.markdown(resume_markdown, unsafe_allow_html=True)

st.divider()


frontend.resume_view_and_download()



