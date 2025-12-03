from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# history with langchain nomenclature
chat_messages = [
    SystemMessage(content="You are a helpful Tutor"),
    HumanMessage(content="Tell me what is 3D plane")
]

result = chat_model.invoke(chat_messages)
ai_msg = AIMessage(content=result.content)
chat_messages.append(ai_msg)

print(chat_messages)