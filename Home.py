import streamlit as st
import streamlit.components.v1 as components
import utils.backend_utils as backend, utils.frontend_utils as frontend
import time

st.set_page_config(layout='wide', page_title='Home', page_icon=":house:")

frontend.load_css()

frontend.create_sidebar()

st.markdown("<h1 class='animated-widget' style='text-align: center; color: white;'>Osher Boudara</h1>", unsafe_allow_html=True)


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


# components.html("""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
#     </head>
#     <h1>
#         <div style='text-align: center; color: white;' id="typed-output" style="font-size:24px; font-weight:bold;"></div>
#         <script>
#             var typed = new Typed('#typed-output', {
#                 strings: ["Hello!", "Welcome to Osher's Resume Website!"],
#                 typeSpeed: 50,
#                 backSpeed: 30,
#                 loop: true
#             });
#         </script>
#     </h1>
#     </html>
#     """, height=50)





