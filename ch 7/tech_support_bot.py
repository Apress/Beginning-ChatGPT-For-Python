"""
tech_support_bot.py

A Discord bot integrated with ChatGPT for automated responses in a designated channel.

This script initializes a Discord bot using the discord.Client() class and listens for events
such as messages being sent. When a message is received in the specified channel, the bot calls
ChatGPT to generate a response based on the message content, and sends the response back to
the same channel.

Requirements:
- discord (https://pypi.org/project/discord.py/)
- chatgpt_client (Assumed to be a custom module providing interaction with ChatGPT)

Usage:
1. Replace the DISCORD_TOKEN variable with your bot's token obtained from the Discord Developer
   Portal.
2. Adjust the CHANNEL_TO_WATCH variable to specify the name of the channel the bot should monitor
   and interact with.
3. Ensure that the chatgpt_client module is properly implemented and accessible.

Note: This script assumes the presence of a chatgpt_client module for interaction with the
      ChatGPT API.
"""


import discord
# import chatgpt_client_for_qa_and_moderation
from chatgpt_client_for_qa_and_moderation import ChatGPTClient

# Bot's token for authentication
DISCORD_TOKEN = 'MTE1OTA4MTg2NzU2ODQ5MjYwNg.GUP_jh.69S5RyGpvHkD6TfsPmRhfUYetnFH3B75sNu208'

# Name of the channel the bot should monitor and interact with
CHANNEL_TO_WATCH = 'q-and-a'

# Initialize the Discord client
discord_client = discord.Client()

# Create the system message for ChatGPT
system_message_to_chatgpt = "You are a virtual assistant that provides support for the Crooks Bank banking app."

with open('FAQ.txt', 'r', encoding='utf-8') as file:
    # Read the entire content of the file into a variable as a single string
    file_contents = file.read()

# Initialize the ChatGPT client
chatgpt_client_for_qa_and_moderation = ChatGPTClient(system_message_to_chatgpt, file_contents)

# Event handler for when the bot is ready
@discord_client.event
async def on_ready():
    """
    Event handler triggered when the bot is successfully logged in and ready to receive events.
    """
    print('Logged in as', discord_client.user)
    print('------')

# Event handler for when a message is received
@discord_client.event
async def on_message(message):
    """
    Event handler triggered when a message is received.

    Parameters:
        message (discord.Message): The message received by the bot.

    Returns:
        None
    """
    # Ignore messages sent by the bot to prevent self-responses
    if message.author == discord_client.user:
        return

    # Ignore messages not in the specified "tech-support" channel
    if isinstance(message.channel, discord.TextChannel) and \
    message.channel.name != CHANNEL_TO_WATCH:
        return
    
    async with message.channel.typing():
        # Call ChatGPT to generate a response based on the received message
        response_from_chatgpt = chatgpt_client_for_qa_and_moderation.send_message_from_discord(message.content)

    # Construct a reply mentioning the message author and appending ChatGPT's response
    reply = f'{message.author.mention} {response_from_chatgpt}'

    # Send the reply to the same channel where the original message was received
    await message.channel.send(reply)

# Run the bot with the provided token
discord_client.run(DISCORD_TOKEN)
