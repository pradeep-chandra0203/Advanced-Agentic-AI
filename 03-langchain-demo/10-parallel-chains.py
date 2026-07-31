from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)

prompt1=ChatPromptTemplate.from_template("What is the capital of {country}?")

prompt2=ChatPromptTemplate.from_template("What is the population of {country}?")

chain1 = prompt1 | model | StrOutputParser()

chain2 = prompt2 | model | StrOutputParser()

parallel_chain = RunnableParallel({
    "capital": chain1,
    "population": chain2
})

result = parallel_chain.invoke({"country": "France"})
print(result)
