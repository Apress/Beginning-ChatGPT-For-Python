"""
content_moderation_bot.py

A Discord bot integrated with ChatGPT and a moderation service for automated content moderation in Discord servers.

This script initializes a Discord bot using the discord.Client() class and listens for events such as messages being sent. When a message is received, it calls both the ChatGPT API and a moderation service to analyze the message content for rule violations. If the message is flagged by either service, it deletes the message and sends a notification to the user explaining why it was deemed inappropriate.

Requirements:
- discord (https://pypi.org/project/discord.py/)
- chatgpt_client_for_qa_and_moderation (Assumed to be a custom module providing interaction with ChatGPT)
- moderation_client (Assumed to be a custom module providing interaction with a moderation service)

Usage:
1. Replace the DISCORD_TOKEN variable with your bot's token obtained from the Discord Developer Portal.
2. Ensure that the chatgpt_client_for_qa_and_moderation and moderation_client modules are properly implemented and accessible.

Note: This script assumes the presence of modules for interaction with ChatGPT and a moderation service.
"""

import discord
from chatgpt_client_for_qa_and_moderation import ChatGPTClient
from moderation_client import ModerationResponse

# Bot's token for authentication
DISCORD_TOKEN = 'YOUR-TOKEN-HERE'

# Initialize the Discord client
discord_client = discord.Client()

# Create the system message for ChatGPT
system_message_to_chatgpt = """
        You are the automated moderator assistant for a Discord server. 
        Review each message for the following rule violations:
        1. Sensitive information
        2. Abuse
        3. Inappropriate comments
        4. Spam, for example; a message in all capital letters, the same phrase or word being repeated over and over, more than 3 exclamation marks or question marks.
        5. Advertisement
        6. External links
        7. Political messages or debate
        8. Religious messages or debate
        
        If any of these violations are detected, respond with "FLAG" (in uppercase without quotation marks). If the message adheres to the rules, respond with "SAFE" (in uppercase without quotation marks).
        """

initial_instructions_to_chatgpt = "Analyze the following message for rule violations:"

# Initialize the ChatGPT client
chatgpt_client_for_qa_and_moderation = ChatGPTClient(system_message_to_chatgpt, initial_instructions_to_chatgpt)

# Initialize the Moderation client
moderation_client = ModerationResponse()

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

    # Call the Moderation method to check for harmful content
    moderation_response = moderation_client.moderate_text(message.content)

    # Call ChatGPT to generate a response based on the received message
    response_from_chatgpt = chatgpt_client_for_qa_and_moderation.send_message_from_discord(message.content)

    # Check for if the message from ChatGPT is "FLAG" or if the moderation response indicates that the input has been flagged
    if response_from_chatgpt == "FLAG" or moderation_response.results[0].flagged:
    
    # Delete the message
        await message.delete()

        # Mention the user who sent the inappropriate message
        author_mention = message.author.mention

        # Send a message mentioning the user and explaining why it was inappropriate
        await message.channel.send(f"{author_mention} This comment was deemed inappropriate for this channel. " +
        "If you believe this to be in error, please contact one of the human server moderators.")


# Run the bot with the provided token
discord_client.run(DISCORD_TOKEN)
