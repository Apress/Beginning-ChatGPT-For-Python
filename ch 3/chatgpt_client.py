"""
Script to demonstrate API call using OpenAI's GPT-4 for chat completions.
"""

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

#instantiate the OpenAI object
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a Python developer"
        },
        {
            "role": "user",
            "content": "Why is Python typically used for data science?"
        }
    ],
    temperature=0.85,
    max_tokens=1921,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
