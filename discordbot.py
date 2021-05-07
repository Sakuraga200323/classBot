
import ast
import asyncio
import cv2
from datetime import datetime, timedelta, timezone
import math
import os
import random
import re
import signal
import sys
import traceback

import discord
from discord.ext import tasks, commands
import psutil
import psycopg2, psycopg2.extras
import traceback

client = discord.Client(intents=discord.Intents.all())
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print("Ready!!")

@client.event
async def on_message(msg):
    if msg.content.startswith("t."):
        if msg.content == "t.ping":
            await msg.channel.send("Pong!!");


client.run(token)
