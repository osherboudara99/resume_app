import streamlit as st
import utils.backend_utils as backend
import utils.frontend_utils as frontend
import utils.chatbot_utils as chatbot

st.set_page_config(layout="wide", page_icon=':office_worker:')
frontend.load_css()
chatbot.create_sidebar()