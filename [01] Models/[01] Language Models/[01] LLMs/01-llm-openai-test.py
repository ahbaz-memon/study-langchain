from langchain_openai import OpenAI
from dotenv import load_dotenv

# load secret keys
load_dotenv()

llm_model = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm_model.invoke("What is the capital of India")
print(result)