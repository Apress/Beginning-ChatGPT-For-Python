import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Define prompt and size
prompt = "A fork in the road on a highway in Washington. There's a roadsign that has arrows, one to Three Oaks, one to Casper and one to Whitechapel"
size = "1024x1024"

# Generate image using DALL·E
response = openai.images.generate(
    prompt=prompt,
    size=size,
    model="dall-e-3"
)


print("Image URL:", response.data[0].url)
