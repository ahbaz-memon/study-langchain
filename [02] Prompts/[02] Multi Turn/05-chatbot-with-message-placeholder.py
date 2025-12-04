from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# current day conversation
chat_message_prompt_template = ChatPromptTemplate([
    ('system', "You are a helpful cutomer support agent"),
    MessagesPlaceholder(variable_name='old_chat_messages'),
    ('human', '{query}'),
])

# load old conversation
with open('../../Data/customer-chat-history.txt') as f:
    old_chat_messages = f.readlines()

chat_message_prompt = chat_message_prompt_template.invoke({
    'old_chat_messages': old_chat_messages,
    'query': "where is my refund ?",
})
print(chat_message_prompt)