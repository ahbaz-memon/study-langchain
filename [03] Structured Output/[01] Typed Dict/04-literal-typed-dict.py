from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# loading review
with open('../../Data/review-1.txt') as f:
    lines = f.readlines()
    review = ' '.join(lines)

# review structure
class Review(TypedDict):
    product_name: Annotated[str, "Name of the product"]
    summary: Annotated[str, "A brief summary of the product"]
    key_themes: Annotated[list[str], "The main features discussed in review"]
    sentiment: Annotated[Literal["pos", "neg"], "Sentiment of the review either negative or positive"]
    pros: Annotated[Optional[list[str]], "List down all pros"]
    cons: Annotated[Optional[list[str]], "List down all cons"]

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

structured_chat_model = chat_model.with_structured_output(Review)

result = structured_chat_model.invoke(review)
print(result)