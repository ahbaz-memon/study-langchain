from langchain_openai import OpenAI
from dotenv import load_dotenv

# load secret keys
load_dotenv()

# temperature controls the randomness and creativity of the output text.
llm_model = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.2)

result = llm_model.invoke("What is the capital of India")
print(result)