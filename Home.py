import streamlit as st
import streamlit.components.v1 as components
import utils.backend_utils as backend, utils.frontend_utils as frontend
import time

st.set_page_config(layout='wide', page_title='Home', page_icon=":house:")

frontend.load_css()

frontend.create_sidebar()

st.markdown("<h1 class='animated-widget' justify-content: center; style='text-align: center; color: white;'>Osher Boudara</h1>", unsafe_allow_html=True)


st.markdown("""<div style="display: flex; justify-content: center; align-items: center; gap: 10px;"> 
            <a href="https://www.linkedin.com/in/osher-boudara-a612921b5/" target="_blank">
    <svg width="30" height="30" viewBox="0 0 24 24" fill="black" xmlns="http://www.w3.org/2000/svg">
        <!-- White Background -->
        <rect width="50" height="30" fill="white"/>
        <path d="M4.98 3.5C4.98 4.88 3.87 6 2.49 6S0 4.88 0 3.5 1.11 1 2.49 1 4.98 2.12 4.98 3.5zM.5 8H4.5V22H.5V8zM8.5 8H12V10H12.04C12.9 8.8 14.15 8 16.04 8 20.5 8 22 10.74 22 14.88V22H18V15.88C18 13.98 17.44 12.88 15.79 12.88 14.13 12.88 13.5 14 13.5 15.88V22H9.5V8H8.5Z"/>
    </svg> 
</a> | 
<a href="https://www.github.com/osherboudara99/" target="_blank">
    <svg width="30" height="30" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 0C5.37 0 0 5.37 0 12C0 17.3 3.44 21.8 8.2 23.3C8.8 23.4 9 23.1 9 22.8V20.7C5.9 21.4 5.2 19.4 5.2 19.4C4.6 18 3.8 17.6 3.8 17.6C2.7 16.9 3.9 17 3.9 17C5.1 17.1 5.7 18.3 5.7 18.3C6.8 20.1 8.5 19.6 9.2 19.3C9.3 18.5 9.6 17.9 9.9 17.6C7.2 17.3 4.4 16.3 4.4 11.6C4.4 10.3 4.9 9.2 5.7 8.3C5.5 8 5.1 6.7 5.9 5C5.9 5 6.9 4.6 9 6.1C10 5.8 11 5.7 12 5.7C13 5.7 14 5.8 15 6.1C17.1 4.6 18.1 5 18.1 5C18.9 6.7 18.5 8 18.3 8.3C19.1 9.2 19.6 10.3 19.6 11.6C19.6 16.3 16.8 17.3 14.1 17.6C14.6 18 15 18.7 15 19.7V22.8C15 23.1 15.2 23.4 15.8 23.3C20.6 21.8 24 17.3 24 12C24 5.37 18.63 0 12 0Z"/>
    </svg> 
</a> </div>""", unsafe_allow_html=True)

time.sleep(3)

# Use `components.html` to properly execute JavaScript
components.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
    </head>
    <h2 style='text-align: center; color: white;'>
        <div style="font-size:24px; font-weight:bold;">
            <span>I am </span><span id="typed-text" ></span>
        </div>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                var typed = new Typed('#typed-text', {
                    strings: ["a Python Developer.", "a Data Scientist.", "a Solutions Architect.", 
                "a Data Engineer.", "a Software Engineer.", "a Machine Learning Engineer.", "a Streamlit Enthusiast."],
                    typeSpeed: 100,
                    backSpeed: 50,
                    loop: true,
                    showCursor: false,
                    backDelay: 1000
                });
            });
        </script>
        </script>

    </h2>
    </html>
    """, height=60)





