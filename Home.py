import streamlit as st
from PIL import Image
from utils.lottie_helper import load_lottie_url
import streamlit_lottie as st_lottie

st.set_page_config(page_title="Home", layout="wide")

# Intro
col1, col2 = st.columns([1, 2])
with col1:
    img = Image.open("profile.jpg")
    st.image(img, width=200)

with col2:
    st.title("💜 Thaheer")
    st.subheader("AI Developer | ML Enthusiast | Creator of NeuraMentor")
    st.write("""
    Hi! I'm Thaheer — passionate about building learning tools, solving AI problems, and sharing knowledge.
    """)
    with open("resume.pdf", "rb") as file:
        st.download_button("📄 Download Resume", data=file, file_name="Thaheer_Resume.pdf", mime="application/pdf")

# Lottie Animation
lottie_url = "https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json"  # Feel free to replace
lottie_json = load_lottie_url(lottie_url)
st_lottie.st_lottie(lottie_json, height=250)
