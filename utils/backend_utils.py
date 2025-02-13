import streamlit as st
import gdown 
import os 
from pathlib import Path


# Default Args
dir_path = os.getcwd()
resume_url = 'https://docs.google.com/document/d/1gql8n7U8WHkdLEu6R6wFI41tLWpnY5QiKQCwdsKMlQA/'
resume_directory_path = f"{dir_path}\\resume\\"
resume_name = 'osher_boudara_resume.pdf'
resume_pdf_path = resume_directory_path + resume_name

def read_file_object(markdown_file):
    return Path(markdown_file).read_text()

@st.cache_data
def download_google_doc_file(url, output_file_name):

    return gdown.download(url, output_file_name, quiet=False, fuzzy=True)

@st.cache_data
def download_multiple_google_doc_files(file_path:str=resume_pdf_path, url:str=resume_url, additional_file_formats:list=['pdf', 'md']):
    
    export_str = 'export?format='

    file_extension = file_path.split('.')[1]

    if file_extension not in additional_file_formats:
        additional_file_formats.append(file_extension)

    for format in additional_file_formats:

        export_format = export_str + format

        export_url = url + export_format

        file_path = file_path.split('.')[0] + '.' + format
        
        print(file_path)
        download_google_doc_file(url=export_url, output_file_name=file_path)


@st.cache_data
def pdf_reader(pdf_file):
    with open(pdf_file, "rb") as f:
        PDFbyte = f.read()
    return PDFbyte

@st.cache_data
def read_and_correct_resume_markdown(dir_path = dir_path):

    resume_markdown = read_file_object(fr"{dir_path}\resume\osher_boudara_resume.md")
    email_number_aligned = """
        <p style='text-align: center; font-size: 18px;'>
            <a href='mailto:osherboudara99@gmail.com'>osherboudara99@gmail.com</a> | 818.809.4261
        </p>
    """
    resume_markdown = resume_markdown.replace('# **OSHER BOUDARA**', '')
    resume_markdown = resume_markdown.replace('[osherboudara99@gmail.com](mailto:osherboudara99@gmail.com) | 818.809.4261', '')
    resume_markdown = email_number_aligned + resume_markdown

    resume_markdown = resume_markdown.replace(r'\[\[BR\]\]', '\n Dates:')
    links_index = resume_markdown.find('**LINKEDIN ')
    resume_markdown = resume_markdown[:links_index].rstrip()

    resume_markdown = resume_markdown.replace('\n## *', '--- \n## *')

    links_markdown = """\n --- \n## Links \n | [LinkedIn Profile](https://www.linkedin.com/in/osher-boudara-a612921b5/) | [GitHub Profile](https://www.github.com/osherboudara99/) | [Certifications](https://www.linkedin.com/in/osher-boudara-a612921b5/details/certifications/) |
    [GitHub Work](https://www.github.com/osherboudara-work/) |
    """

    resume_markdown = resume_markdown + links_markdown 
    return resume_markdown