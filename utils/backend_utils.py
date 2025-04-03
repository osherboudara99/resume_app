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
    resume_markdown = resume_markdown.replace("â€™", "'")
    resume_markdown = email_number_aligned + resume_markdown

    resume_markdown = resume_markdown.replace(r'\[\[BR\]\]', '\n Dates:')
    links_index = resume_markdown.find('**LINKEDIN ')
    resume_markdown = resume_markdown[:links_index].rstrip()

    resume_markdown = resume_markdown.replace('\n## *', '--- \n## *')

    links_markdown = """\n --- \n## Links \n 
| <a href="https://www.linkedin.com/in/osher-boudara-a612921b5/" target="_blank">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="black" xmlns="http://www.w3.org/2000/svg">
        <!-- White Background -->
        <rect width="24" height="24" fill="white"/>
        <path d="M4.98 3.5C4.98 4.88 3.87 6 2.49 6S0 4.88 0 3.5 1.11 1 2.49 1 4.98 2.12 4.98 3.5zM.5 8H4.5V22H.5V8zM8.5 8H12V10H12.04C12.9 8.8 14.15 8 16.04 8 20.5 8 22 10.74 22 14.88V22H18V15.88C18 13.98 17.44 12.88 15.79 12.88 14.13 12.88 13.5 14 13.5 15.88V22H9.5V8H8.5Z"/>
    </svg> LinkedIn
</a> | 
<a href="https://www.github.com/osherboudara99/" target="_blank">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 0C5.37 0 0 5.37 0 12C0 17.3 3.44 21.8 8.2 23.3C8.8 23.4 9 23.1 9 22.8V20.7C5.9 21.4 5.2 19.4 5.2 19.4C4.6 18 3.8 17.6 3.8 17.6C2.7 16.9 3.9 17 3.9 17C5.1 17.1 5.7 18.3 5.7 18.3C6.8 20.1 8.5 19.6 9.2 19.3C9.3 18.5 9.6 17.9 9.9 17.6C7.2 17.3 4.4 16.3 4.4 11.6C4.4 10.3 4.9 9.2 5.7 8.3C5.5 8 5.1 6.7 5.9 5C5.9 5 6.9 4.6 9 6.1C10 5.8 11 5.7 12 5.7C13 5.7 14 5.8 15 6.1C17.1 4.6 18.1 5 18.1 5C18.9 6.7 18.5 8 18.3 8.3C19.1 9.2 19.6 10.3 19.6 11.6C19.6 16.3 16.8 17.3 14.1 17.6C14.6 18 15 18.7 15 19.7V22.8C15 23.1 15.2 23.4 15.8 23.3C20.6 21.8 24 17.3 24 12C24 5.37 18.63 0 12 0Z"/>
    </svg> Personal Github
</a> |
<a href="https://www.github.com/osherboudara-work/" target="_blank">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 0C5.37 0 0 5.37 0 12C0 17.3 3.44 21.8 8.2 23.3C8.8 23.4 9 23.1 9 22.8V20.7C5.9 21.4 5.2 19.4 5.2 19.4C4.6 18 3.8 17.6 3.8 17.6C2.7 16.9 3.9 17 3.9 17C5.1 17.1 5.7 18.3 5.7 18.3C6.8 20.1 8.5 19.6 9.2 19.3C9.3 18.5 9.6 17.9 9.9 17.6C7.2 17.3 4.4 16.3 4.4 11.6C4.4 10.3 4.9 9.2 5.7 8.3C5.5 8 5.1 6.7 5.9 5C5.9 5 6.9 4.6 9 6.1C10 5.8 11 5.7 12 5.7C13 5.7 14 5.8 15 6.1C17.1 4.6 18.1 5 18.1 5C18.9 6.7 18.5 8 18.3 8.3C19.1 9.2 19.6 10.3 19.6 11.6C19.6 16.3 16.8 17.3 14.1 17.6C14.6 18 15 18.7 15 19.7V22.8C15 23.1 15.2 23.4 15.8 23.3C20.6 21.8 24 17.3 24 12C24 5.37 18.63 0 12 0Z"/>
    </svg> Work Github
</a> |
[📜 All Certifications](https://www.linkedin.com/in/osher-boudara-a612921b5/details/certifications/)
"""

    resume_markdown = resume_markdown + links_markdown 
    return resume_markdown