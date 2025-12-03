from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# history with langchain nomenclature
chat_message_prompt_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert"),
    ('human', 'Explain in simple terms, what is {topic}'),
])

chain = chat_message_prompt_template | chat_model

result = chain.invoke({
    'domain': 'cricket',
    'topic': 'not-out',
})
print(result.content)