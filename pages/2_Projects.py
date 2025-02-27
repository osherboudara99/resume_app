import streamlit as st
import utils.backend_utils as backend
import utils.frontend_utils as frontend

st.set_page_config(layout="wide", page_icon=':office_worker:')
frontend.load_css()
frontend.create_sidebar()