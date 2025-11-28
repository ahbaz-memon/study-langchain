from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Python is a popular framework",
    "Lion is a animal",
    "Tiger is a animal"
]
result = embedding_model.embed_documents(documents)
print(str(result))