from pydantic import BaseModel, Field
from typing import Literal
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class Feedback(BaseModel):
    name: str = Field(description="Name of the participant")
    summary: str
    sentiment: Literal["positive", "negative"]
    rating: int
    email: str

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.parse(
    model="gpt-4o-mini",
    input=[
        {
            "role": "system",
            "content": "Extract the feedback into the given schema."
        },
        {
            "role": "user",
            "content": """
            The Java Fullstack training was excellent.
            Trainer was very knowledgeable.
            I would rate it 4 out of 5.
            My name is Dhiraj Kumar.
            My email is dhiraj2001@gmail.com.
            """
        }
    ],
    text_format=Feedback,
)

print(response.output_parsed)

def main():
    print("Hello from 02-structured-output!")


if __name__ == "__main__":
    main()
