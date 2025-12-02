import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


st.header("Research Tool")

user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    result = chat_model.invoke(user_input)
    st.write(result.content)