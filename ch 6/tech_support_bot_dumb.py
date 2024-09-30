import discord

# Bot's token for authentication
discord_token = 'YOUR-TOKEN-HERE'

# Name of the channel the bot should monitor and interact with
channel_to_watch = 'q-and-a'

# Initialize the Discord client
discord_client = discord.Client()

# Event handler for when the bot is ready
@discord_client.event
async def on_ready():
    print('Logged in as', discord_client.user)
    print('------')

# Event handler for when a message is received
@discord_client.event
async def on_message(message):
    # Ignore messages sent by the bot to prevent self-responses
    if message.author == discord_client.user:
        return

    # Ignore messages not in the specified "q-and-a" channel
    if isinstance(message.channel, discord.TextChannel) and message.channel.name != channel_to_watch:
        return

    # Send a greeting response to the user who sent the message
    reply = f'hi {message.author.mention}, I can help you with that!'
    await message.channel.send(reply)

# Run the bot with the provided token
discord_client.run(discord_token)
