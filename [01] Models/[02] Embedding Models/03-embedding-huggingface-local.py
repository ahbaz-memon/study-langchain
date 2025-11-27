import os
from sklearn.metrics.pairwise import cosine_similarity
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['HF_HOME'] = "D:/Future Code Study Folder/Libraries/LangChain/Models/HuggingFace Cache"

embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# text = "Delhi is the capital of India"

# result = embedding_model.embed_query(text)
# print(result)

query = "Django uses Python framework"
documents = [
    "Python is a popular framework",
    "Lion is a animal",
    "Tiger is a animal"
]

query_vector = embedding_model.embed_query(query)
docs_vector = embedding_model.embed_documents(documents)

print(cosine_similarity([query_vector], docs_vector))