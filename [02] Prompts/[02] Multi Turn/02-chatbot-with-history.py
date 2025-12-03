from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# a simple chatbot with history
chat_history = []
while True:
    user_input = input('You: ').strip()
    chat_history.append(user_input)

    if user_input in ["exit", 'e', "quit", "q"]:
        break
    
    result = chat_model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)