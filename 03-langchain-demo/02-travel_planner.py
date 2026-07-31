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

template = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful assistant."),
        (
            "user",
             """"
    You are a professional travel planner. Based on the user's profile, create a personalized travel itinerary. Include activities, must-see attractions, suggested local food, transportation tips, cultural do's and don't's and a basic packing checklist.

    User Info:
    - Name: {username}
    - Destination: {destination}
    - Travel Date: {start_date} to {end_date}
    - Budget: {budget}
    - Interest: {interests}
    - Travel Style: {travel_style}
    - Dietary Preferences: {dietary_preferences}

    Ensure the plan fits the user's budget and travel style. Highlight one unique or offbeat experience they shouldn't miss.
    Keep the tone friendly and informative.
    """,
        ),
    ],
    validate_template=True,
)

prompt = template.invoke(
    {
        "username": "Pradeep",
        "destination": "Japan",
        "start_date": "2026-10-01",
        "end_date": "2026-10-10",
        "budget": "$3000",
        "interests": "Technology, Temples, Anime",
        "travel_style": "Luxury",
        "dietary_preferences": "Vegetarian",
    }
)

response = model.invoke(prompt)
print(response.content)