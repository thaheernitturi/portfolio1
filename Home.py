import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import streamlit_lottie as st_lottie

# Load Lottie Animation
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            st.warning(f"Failed to load Lottie animation from {url}")
            return None
        return r.json()
    except Exception as e:
        st.error(f"Error loading Lottie from {url}: {e}")
        return None

# Load Lottie animations
lottie_ai = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_1pxqjqps.json")
lottie_projects = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tno6cg2w.json")
lottie_contact = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json")

# --- PAGE CONFIG ---
st.set_page_config(page_title="Thaheer Nitturi | Portfolio", page_icon=":brain:", layout="wide")

# --- HEADER SECTION ---
st.subheader("Hi, I'm Thaheer Nitturi :wave:")
st.title("Aspiring AI Researcher | ML Developer | Innovator")
st.write("I'm a final-year B.Tech student at NIT Trichy passionate about building intelligent systems that solve real-world problems.")
st.write("---")

# --- ABOUT ME ---
st.header("About Me")
left_col, right_col = st.columns(2)
with left_col:
    st.write("""
        - 🎓 Pursuing B.Tech in Instrumentation and Control Engineering at NIT Trichy (2021–2025)
        - 🧠 Passionate about Machine Learning, AI Research, and Startups
        - 🤖 Built multiple projects in computer vision, NLP, and educational tech
        - 📍 Currently working on NeuraMentor – an AI-powered ML tutor
    """)
with right_col:
    if lottie_ai:
        st_lottie.st_lottie(lottie_ai, height=250, key="ai")
    else:
        st.info("AI animation not available.")

st.write("---")

# --- PROJECTS ---
st.header("Projects")
st.subheader("1. NeuraMentor – AI ML Tutor")
st.write("""
An AI-powered learning platform that teaches machine learning like a personal tutor. Built with Streamlit, LangChain, and OpenAI API.
- 🧠 Custom embeddings for topic structuring
- 🎯 Personalized quiz generation and topic recommendations
- 📊 Built-in code editor for live coding
""")

st.subheader("2. Vision-based Gesture Controlled Interface")
st.write("""
A system that detects hand gestures using OpenCV and maps them to actions (like volume control).
- ✋ Real-time finger detection
- 🔄 Gesture-action mapping
""")

st.subheader("3. Object Tracking System")
st.write("""
Tracks moving objects in real time using Kalman Filter and OpenCV.
- 🎥 Frame-by-frame object detection
- 📍 Real-time position tracking
""")

if lottie_projects:
    st_lottie.st_lottie(lottie_projects, height=200, key="projects")
else:
    st.info("Project animation not available.")

st.write("---")

# --- EXPERIENCE & EDUCATION ---
st.header("Experience & Education")
st.write("""
**Intern, DRDO – Defense Research and Development Organisation**  
- Built a multi-modal detection pipeline for real-time human detection  

**B.Tech – NIT Trichy (2021–2025)**  
- Department of Instrumentation and Control Engineering  
- CGPA: 8.43 (as of 6th semester)
""")

st.write("---")

# --- SKILLS ---
st.header("Skills")
st.write("""
- **Languages**: Python, SQL, C++
- **ML Libraries**: PyTorch, TensorFlow, scikit-learn
- **Tools**: OpenCV, Streamlit, Git, LangChain, FastAPI
- **Platforms**: GitHub, Hugging Face, Google Colab
""")

st.write("---")

# --- TESTIMONIALS ---
st.header("Testimonials")
st.info("\"Thaheer has an exceptional drive for learning and building real-world AI systems. His commitment to NeuraMentor shows his innovation and ability to bring ideas to life.\" – Mentor")

st.write("---")

# --- CONTACT ---
st.header("Contact Me")
if lottie_contact:
    st_lottie.st_lottie(lottie_contact, height=150, key="contact")
else:
    st.info("Contact animation not available.")
st.write("Feel free to reach out!")
contact_form = """
<form action="https://formsubmit.co/thaheer@example.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required><br><br>
    <input type="email" name="email" placeholder="Your Email" required><br><br>
    <textarea name="message" placeholder="Your message here..." required></textarea><br><br>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.markdown("Made with ❤️ by Thaheer Nitturi")
