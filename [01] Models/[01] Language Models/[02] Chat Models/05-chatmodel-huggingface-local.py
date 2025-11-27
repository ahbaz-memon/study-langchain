import os
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

os.environ['HF_HOME'] = "D:/Future Code Study Folder/Libraries/LangChain/Models/HuggingFace Cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
    ),
    device_map='auto',    
)
chat_model = ChatHuggingFace(llm=llm)