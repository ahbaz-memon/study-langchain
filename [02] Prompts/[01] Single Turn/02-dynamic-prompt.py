import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name", options=[
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
])
style_input = st.selectbox("Select Explanation Style", options=[
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical",
])
length_input = st.selectbox("Select Explanation Length", options=[
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)",
])