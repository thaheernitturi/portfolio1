import streamlit as st

st.set_page_config(page_title="Projects")

st.title("🚀 My Projects")

projects = [
    {
        "title": "NeuraMentor",
        "desc": "An AI-powered platform to teach machine learning like a personal tutor.",
    },
    {
        "title": "Smart Diet Planner",
        "desc": "GPT-based personalized fat-loss meal planner.",
    },
    {
        "title": "Lavender Portfolio",
        "desc": "This beautiful portfolio site built in Streamlit!",
    }
]

for project in projects:
    st.subheader(project["title"])
    st.write(project["desc"])
    st.markdown("---")
