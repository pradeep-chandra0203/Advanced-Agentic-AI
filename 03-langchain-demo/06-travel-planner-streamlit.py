import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from travel_planner_template_generated import template
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini"
)

st.header("Travel Planner")

username = st.text_input("Name")
destination = st.text_input("Destination")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
budget = st.slider("Select Budget", 10000, 1000000)

interest = st.multiselect(
    "Interests",
    ["Adventure", "Beaches", "Nature", "Shopping"]
)

travel_style = st.multiselect(
    "Travel Style",
    ["Luxury", "Solo", "Group", "Family"]
)

dietary_preferences = st.selectbox(
    "Dietary Preferences",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

chain = template | model | StrOutputParser()

if st.button("Generate Plan"):
    st.write_stream(chain.stream({
        "username": username,
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "budget": budget,
        "interests": interest,
        "travel_style": travel_style,
        "dietary_preferences": dietary_preferences,
    }))


  # run using this uv run streamlit run 06-travel-planner-streamlit.py  