import streamlit as st

st.sidebar.image('self.jpeg')
st.sidebar.markdown("## __About Osher__")
st.markdown("<h1 style='text-align: center; color: white;'>Osher's Resume</h1>", unsafe_allow_html=True)


about = "My name is Osher Boudara and I am a data scientist with a passion for transforming dataframes into actionable insights. \
With a background in computer science and statistics, I specialize in building robust machine learning algorithms and conducting statistical analysis of datasets. \
My expertise in Python, SQL and cloud-based architectures have allowed me to develop scalable tools that provide unique solutions to stakeholders."
with st.sidebar.expander('About Osher', expanded=False):
    st.sidebar.write(about)