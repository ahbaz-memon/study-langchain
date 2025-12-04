from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# current day conversation
chat_message_prompt_template = ChatPromptTemplate([
    ('system', "You are a helpful cutomer support agent"),
    MessagesPlaceholder(variable_name='old_chat_messages')
    ('human', '{query}'),
])