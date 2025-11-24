from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# a end-point from HuggingFace to us
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("What is the capital of India")

# result is dict which have metadata too
print(result.content)