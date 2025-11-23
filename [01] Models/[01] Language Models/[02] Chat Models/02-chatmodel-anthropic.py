from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic("claude-3-5-sonnet-20241022")

result = chat_model.invoke("What is the capital of India")

# result is dict which have metadata too
print(result.content)