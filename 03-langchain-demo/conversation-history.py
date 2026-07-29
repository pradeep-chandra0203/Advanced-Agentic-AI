import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)

conversation_history = []
while True:
    user_input = input("User: ")
    conversation_history.append({"role": "user", "content": user_input})
    if user_input.lower() == "exit":
        break
    response = model.invoke(conversation_history)
    print("Assistant:", response.content)
    conversation_history.append({"role": "assistant", "content": response.content})

