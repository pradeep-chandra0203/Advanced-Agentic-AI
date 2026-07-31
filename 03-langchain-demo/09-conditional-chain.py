from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import Literal
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="The sentiment of the feedback"
    )

pyparser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = ChatPromptTemplate(
    [
        ("system", "You are a sentiment analyzer."),
        ("human", "Analyze the sentiment of the following feedback: {feedback}\n{format_instructions}"),
    ],
    input_variables=["feedback"],
    partial_variables={"format_instructions": pyparser.get_format_instructions()},
    validate_template=True,
)

chain1 = prompt1 | model | pyparser

positive_email_prompt = ChatPromptTemplate.from_template(
    "Write an email to the customer thanking them for their positive feedback: {feedback}"
)

negative_email_prompt = ChatPromptTemplate.from_template(
    "Write an email to the customer apologizing for their negative feedback: {feedback}"
)

branch_chain = RunnableBranch(
    (lambda x: x["analysis"].sentiment == "positive",
     positive_email_prompt | model | StrOutputParser()),
    (lambda x: x["analysis"].sentiment == "negative",
     negative_email_prompt | model | StrOutputParser()),
    lambda x: "not able to analyse feedback"
)

chain = {
    "analysis": chain1,
    "feedback": RunnablePassthrough()
} | branch_chain

result = chain.invoke({"feedback": "I love this product!"})
print(result)