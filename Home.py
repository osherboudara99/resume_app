import pandas as pd 
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from pathlib import Path

from resume_pdf_downloader import  download_google_doc_file


st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Osher's Resume App</h1>", unsafe_allow_html=True)
st.sidebar.image('self.jpeg')
st.sidebar.markdown("## __About Osher__")
st.markdown("<h1 style='text-align: center; color: white;'>Osher's Resume</h1>", unsafe_allow_html=True)


about = "I am a data scientist with a passion for transforming dataframes into actionable insights. \
With a background in computer science and statistics, I specialize in building robust machine learning algorithms and conducting statistical analysis of any dataset that comes my way. \
My expertise in Python, SQL and cloud-based architectures have allowed me to develop scalable tools that provide unique solutions."

st.sidebar.write(about)

resume_url_pdf = "https://docs.google.com/document/d/1gql8n7U8WHkdLEu6R6wFI41tLWpnY5QiKQCwdsKMlQA/export?format=pdf"

resume_name_pdf = 'osher_resume.pdf'

resume_url_md = "https://docs.google.com/document/d/1gql8n7U8WHkdLEu6R6wFI41tLWpnY5QiKQCwdsKMlQA/export?format=md"

resume_name_md = 'osher_resume.md'

download_google_doc_file(resume_url_pdf, resume_name_pdf)
download_google_doc_file(resume_url_md, resume_name_md)


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

intro_markdown = read_markdown_file("osher_resume.md")
email_number_aligned = """
    <p style='text-align: center; font-size: 18px;'>
        <a href='mailto:osherboudara99@gmail.com'>osherboudara99@gmail.com</a> | 818.809.4261
    </p>
"""
intro_markdown = intro_markdown.replace('# **OSHER BOUDARA**', '')
intro_markdown = intro_markdown.replace('[osherboudara99@gmail.com](mailto:osherboudara99@gmail.com) | 818.809.4261', '')
intro_markdown = email_number_aligned + intro_markdown

intro_markdown = intro_markdown.replace(r'\[\[BR\]\]', '\n Dates:')
links_index = intro_markdown.find('**LINKEDIN ')
intro_markdown = intro_markdown[:links_index].rstrip()

intro_markdown = intro_markdown.replace('\n## *', '--- \n## *')

links_markdown = """
--- \n## Links 
| [LinkedIn Profile](https://www.linkedin.com/in/osher-boudara-a612921b5/) | [GitHub Profile](https://www.github.com/osherboudara99/) | [Certifications](https://www.linkedin.com/in/osher-boudara-a612921b5/details/certifications/) |
 [GitHub Work](https://www.github.com/osherboudara-work/) |
"""

intro_markdown = intro_markdown + links_markdown 
st.markdown(intro_markdown, unsafe_allow_html=True)


st.divider()

with st.expander('View Resume PDF'):
    pdf_viewer(resume_name_pdf)

@st.cache_data
def resume_reader(resume_name=resume_name_pdf):
    with open(resume_name, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    return PDFbyte

st.download_button("Download Resume", data=resume_reader(), file_name='osher_boudara_resume.pdf')


