import streamlit as st
from utils.lottie_helper import load_lottie_url
import streamlit_lottie as st_lottie

st.set_page_config(page_title="Contact")

st.title("📬 Contact Me")

st.write("Reach out to me via any of these platforms:")

st.markdown("""
- 📧 [thaheer@example.com](mailto:thaheer@example.com)  
- 💼 [LinkedIn](https://linkedin.com/in/yourprofile)  
- 🧑‍💻 [GitHub](https://github.com/yourusername)  
""")

lottie_url = "https://assets9.lottiefiles.com/private_files/lf30_tulw6x.json"
lottie_json = load_lottie_url(lottie_url)
st_lottie.st_lottie(lottie_json, height=200)
