from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

result = chat_model.invoke("What is the capital of India")

# result is dict which have metadata too
print(result.content)