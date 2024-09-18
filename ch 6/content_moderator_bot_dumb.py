import discord

# Bot's token for authentication
discord_token = 'MTE2MTI3NDk1NDYwMDQxOTMzOQ.GIjVWw.MN9mAWbkv4wLq_nus2vGpGnOAd9fUixMJe07XY'

# Banned word to monitor in messages
banned_word = 'puppies'

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

    # Check if the message was sent in a guild (server)
    if message.guild is not None:
        # Check if the banned word is in the message content
        if banned_word in message.content:
            # Delete the message
            await message.delete()

            # Mention the user who sent the inappropriate message
            author_mention = message.author.mention

            # Send a warning message mentioning the user
            await message.channel.send(f'{author_mention} This comment was deemed inappropriate for this channel. '
                                       f'If you believe this to be in error, please contact one of the human server moderators.')

# Run the bot with the provided token
discord_client.run(discord_token)
