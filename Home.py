import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide', page_title='Home', page_icon=":house:")

import utils.backend_utils as backend, utils.frontend_utils as frontend, utils.chatbot_utils as chatbot
import time
import os


dir_path = os.getcwd()


# Call the function to load the CSS
frontend.load_css()

chatbot.create_sidebar()

st.markdown("<h1 class='animated-widget' justify-content: center; style='text-align: center; color: white;'>Osher Boudara</h1>", unsafe_allow_html=True)


st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; gap: 12px;">

  <div style="background-color: #1e1e3f; padding: 10px; border-radius: 10px;">
    <a href="https://www.linkedin.com/in/osher-boudara-a612921b5/" target="_blank">
      <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="#ffffff">
        <path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5zM0 24h5V7H0v17zm7.5-17h4.7v2.5h.07c.66-1.25 2.3-2.5 4.73-2.5 5.05 0 5.98 3.32 5.98 7.63V24h-5v-7.33c0-1.75-.03-4-2.43-4s-2.8 1.9-2.8 3.87V24h-5V7z"/>
      </svg>
    </a>
  </div>

  <div style="background-color: #1e1e3f; padding: 10px; border-radius: 10px;">
    <a href="https://www.github.com/osherboudara99/" target="_blank">
      <svg width="30" height="30" viewBox="0 0 24 24" fill="#ffffff" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 0C5.37 0 0 5.37 0 12C0 17.3 3.44 21.8 8.2 23.3C8.8 23.4 9 23.1 9 22.8V20.7C5.9 21.4 5.2 19.4 5.2 19.4C4.6 18 3.8 17.6 3.8 17.6C2.7 16.9 3.9 17 3.9 17C5.1 17.1 5.7 18.3 5.7 18.3C6.8 20.1 8.5 19.6 9.2 19.3C9.3 18.5 9.6 17.9 9.9 17.6C7.2 17.3 4.4 16.3 4.4 11.6C4.4 10.3 4.9 9.2 5.7 8.3C5.5 8 5.1 6.7 5.9 5C5.9 5 6.9 4.6 9 6.1C10 5.8 11 5.7 12 5.7C13 5.7 14 5.8 15 6.1C17.1 4.6 18.1 5 18.1 5C18.9 6.7 18.5 8 18.3 8.3C19.1 9.2 19.6 10.3 19.6 11.6C19.6 16.3 16.8 17.3 14.1 17.6C14.6 18 15 18.7 15 19.7V22.8C15 23.1 15.2 23.4 15.8 23.3C20.6 21.8 24 17.3 24 12C24 5.37 18.63 0 12 0Z"/>
      </svg>
    </a>
  </div>

</div>
""", unsafe_allow_html=True)
time.sleep(1.5)

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



img_base64 = backend.get_base64_image(f"{dir_path}/resume/self.jpeg")

# HTML layout with flex row
st.markdown(f"""
<div style="display: flex; flex-direction: row; align-items: center; background-color: #1e1e3f; padding: 30px; border-radius: 15px; color: white; gap: 30px;">
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="{img_base64}" style="width: 200px; border-radius: 12px;" />
    </div>
    <div style="max-width: 850px; font-size: 16px; line-height: 1.6;">
        <p>
        As a Senior Data Scientist at Cognizant, I am leading and developing projects in data science and engineering teams for the crop science division of a global Fortune 500 company. I use my data science skillset to deliver solutions that meet the client's needs and expectations.
        </p>
        <p>
        I have a B.S. in Computer Science and a minor in Statistics from California State University, Northridge, where I graduated with honors. I am passionate about conducting statistical research and transforming dataframes into actionable insights. 
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

import requests

GITHUB_USERNAME = "osherboudara99"

def get_sorted_repos_by_update(username, token=None):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    headers = {"Authorization": f"token {token}"} if token else {}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch repos: {response.status_code}")
        return []

    repos = response.json()
    
    # Sort repos by 'updated_at' (latest first)
    sorted_repos = sorted(repos, key=lambda r: r['updated_at'], reverse=True)

    # Optional: extract useful info for each repo
    formatted_repos = []
    for repo in sorted_repos:
        formatted_repos.append({
            "name": repo["name"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "language": repo["language"],
            "stargazers_count": repo["stargazers_count"],
            "forks_count": repo["forks_count"],
            "updated_at": repo["updated_at"]
        })

    return formatted_repos

def display_repos(repos):
    for repo in repos:
        with st.container():
            st.markdown(f"### [{repo['name']}]({repo['html_url']})")
            st.markdown(f"**Description:** {repo['description'] or 'No description'}")
            st.markdown(f"**Language:** {repo['language'] or 'Not specified'}")
            st.markdown(f"**Last Updated:** {repo['updated_at']}")
            st.markdown(f"⭐ Stars: {repo['stargazers_count']} | 🍴 Forks: {repo['forks_count']}")
            st.markdown("---")

repos = get_sorted_repos_by_update(GITHUB_USERNAME)
display_repos(repos)






