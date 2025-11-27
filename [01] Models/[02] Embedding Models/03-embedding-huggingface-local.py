import os
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['HF_HOME'] = "D:/Future Code Study Folder/Libraries/LangChain/Models/HuggingFace Cache"

embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India"

result = embedding_model.embed_query(text)
print(result)