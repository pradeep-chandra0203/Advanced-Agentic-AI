import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = model.invoke(user_input)
    print("Assistant:", response.content)

