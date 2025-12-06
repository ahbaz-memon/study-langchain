from dotenv import load_dotenv
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# loading review
with open('../../Data/review-1.txt') as f:
    lines = f.readlines()