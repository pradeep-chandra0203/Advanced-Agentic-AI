import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)

template = ChatPromptTemplate([
    ("system", "You are a helpful assistant."),
    ("user", "Write a article about {topic} ")
])

template2 = ChatPromptTemplate([
    ("system", "You are a helpful assistant."),
    ("user", "write 5 mcq's about {article} and Difficulty: {difficulty}")
])

prompt = template.invoke({"topic": "AI"})
#prompt2 = template.invoke({"topic": "Machine Learning"})

#response = model.invoke(prompt2)

#LCEL 

#article_chain = template | model | StrOutputParser()

#chain = {
#    "article": article_chain,
 #   "difficulty": RunnableLambda(lambda _: "Hard")
# | template2 | model | StrOutputParser()

chain = template | model | StrOutputParser() | {"article": RunnablePassthrough(), 
"difficulty": RunnableLambda(lambda _: "Hard")} | template2 | model | StrOutputParser()

response = chain.invoke({"topic": "AI"})
print(response)
