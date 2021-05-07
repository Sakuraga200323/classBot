from discord.ext import commands
import os
import traceback

client = discord.Client
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_message(msg):
    if msg.content.startswith("t."):
        if msg.content == "t.ping":
        await msg.channel.send("Pong!!");


client.run(token)
