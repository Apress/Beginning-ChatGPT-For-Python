import os
from dotenv import load_dotenv
from openai import OpenAI

class ModerationResponse:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI()

    def moderate_text(self, text):
        moderation = self.client.moderations.create(input=text)
        return moderation
