from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# history with langchain nomenclature
chat_messages = [
    SystemMessage(content="You are a helpful Doctor"),
]

# chatbot with langchain messages
while True:
    user_input = input("You: ").strip()
    user_msg = HumanMessage(content=user_input)
    chat_messages.append(user_msg)

    if user_input in ["exit", 'e', "quit", "q"]:
        break

    result = chat_model.invoke(chat_messages)
    ai_msg = AIMessage(content=result.content)
    chat_messages.append(ai_msg)
    print("AI: ", result.content)

print(chat_messages)