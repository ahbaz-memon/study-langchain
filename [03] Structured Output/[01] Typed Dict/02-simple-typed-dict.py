from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# loading review
with open('../../Data/review-1.txt') as f:
    lines = f.readlines()
    review = ' '.join(lines)

# review structure
class Review(TypedDict):
    product_name: str
    summary: str
    sentiment: bool

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")