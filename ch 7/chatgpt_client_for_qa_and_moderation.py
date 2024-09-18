import os
from dotenv import load_dotenv
from openai import OpenAI

class ChatGPTClient:
    def __init__(self, system_message, initial_instructions_to_chatgpt):
        # Load environment variables from .env
        load_dotenv()

        # Use the API key from the environment variable
        self.client = OpenAI()
        self.system_message = system_message
        self.initial_instructions_to_chatgpt = initial_instructions_to_chatgpt

    def send_message_from_discord(self, user_message):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": f'{self.system_message}'
                },
                {
                    "role": "user",
                    "content": f'{self.initial_instructions_to_chatgpt}'
                },
                {
                    "role": "user",
                    "content": f'{user_message}'
                }
            ],
            temperature=0.85,
            max_tokens=1921,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        condensed_response = response.choices[0].message.content
        return condensed_response

