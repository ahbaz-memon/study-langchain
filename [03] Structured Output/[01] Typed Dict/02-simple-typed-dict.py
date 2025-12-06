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

structured_chat_model = chat_model.with_structured_output(Review)

result = structured_chat_model.invoke(review)
print(result)