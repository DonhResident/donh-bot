import os
import json

import datetime

import discord
from discord.ext import commands

from discord_components import *

client = commands.Bot(command_prefix='.', intents=discord.Intents().all())
client.remove_command(help)

async def open_acc(user):
    users = await get_bank()
    if user.bot is True:
        return
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0

    with open('./jsons/bank.json', 'w') as f:
        json.dump(users, f)
        return True

async def get_bank():
    with open('./jsons/bank.json', 'r') as f:
        users = json.load(f)
        return users


@client.event
async def on_ready():
    DiscordComponents(client)
    await client.change_presence(status=discord.Status.idle)
    print(1)
for filename in os.listdir("./cogs"):
  if filename.endswith('.py') and not filename.startswith("_"):
    client.load_extension(f'cogs.{filename[:-3]}')


client.run('Token')
