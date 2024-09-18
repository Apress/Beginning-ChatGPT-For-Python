"""Module for interacting with OpenAI API to list the models available"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Use the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

models_list = client.models.list()

# Iterate through the list and print model information
for model in models_list.data:
    print(f"Model ID: {model.id}")
    print(f"Created: {model.created}")
    print(f"Object: {model.object}")
    print(f"Owned By: {model.owned_by}")
    print("\n============================\n")  # Separator for better readability
