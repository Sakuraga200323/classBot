from discord.ext import commands
import os
import traceback

client = discord.Client(intents=discord.Intents.all())
token = os.environ['DISCORD_BOT_TOKEN']

@clinent.event
async def on_ready():
    print("Ready!!")

@client.event
async def on_message(msg):
    if msg.content.startswith("t."):
        if msg.content == "t.ping":
        await msg.channel.send("Pong!!");


client.run(token)
