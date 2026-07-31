import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from travel_planner_template_generated import template
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)


chain = template | model | StrOutputParser()

for chunk in chain.stream({
        "username": "Pradeep",
        "destination": "Japan",
        "start_date": "2026-10-01",
        "end_date": "2026-10-10",
        "budget": "$3000",
        "interests": "Technology, Temples, Anime",
        "travel_style": "Luxury",
        "dietary_preferences": "Vegetarian",
    }):
        print(chunk, end="")