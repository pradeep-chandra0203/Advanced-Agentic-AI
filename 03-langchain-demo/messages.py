import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)

conversation_history = [
    SystemMessage(content="You are a helpful AI assistant who answers question in a humorous way."),
]
while True:
    user_input = input("you: ")
    conversation_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    response = model.invoke(conversation_history)
    conversation_history.append(AIMessage(content=response.content))
    print(response.content)

print(conversation_history)

