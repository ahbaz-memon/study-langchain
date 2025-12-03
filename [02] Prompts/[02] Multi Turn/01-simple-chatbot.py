from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# a simple chatbot
while True:
    user_input = input('You: ').strip()
    
    if user_input in ["exit", 'e', "quit", "q"]:
        break
    
    result = chat_model.invoke(user_input)
    print("AI: ", result.content)