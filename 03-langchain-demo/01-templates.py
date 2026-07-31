import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)

template = ChatPromptTemplate([
    ("system", "You are a helpful assistant."),
    ("user", "Write a article about {topic} in 100 words")
])

#prompt1 = template.invoke({"topic": "AI"})
#prompt2 = template.invoke({"topic": "Machine Learning"})

#response = model.invoke(prompt2)

#LCEL 

chain = template | model | StrOutputParser()
response = chain.invoke({"topic": "AI"})
print(response)