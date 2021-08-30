# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = commands.Bot(
    command_prefix=commands.when_mentioned_or('-'),
    description="Be unique, be first, be bot!",
)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if 'saulo' in str(message.author).lower():
         await message.add_reaction("🇺🇸")
    await client.process_commands(message)

client.run(TOKEN)