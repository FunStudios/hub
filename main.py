  # This example requires the 'message_content' intent.
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event

async def on_ready():
    print(f'We have logged in as {client.user}')
    activity = discord.Game(name="?cmds or ?help", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?about'):
        await message.channel.send('Hi!')
        await message.channel.send('I am PyBot')
        await message.channel.send('A test robot in python')
        await message.channel.send('Notice: I am a work in progress.')
    if message.content.startswith('?cmds'):
      await message.channel.send('**Commands:**')
      await message.channel.send('?about')
      await message.channel.send('?cmds')
      await message.channel.send('?help')
    
    if message.content.startswith('?help'):
      await message.channel.send('**Help:**')
      await message.channel.send('so we are not going to')
      await message.channel.send('?cmds')
      await message.channel.send('?help')
    if message.content.startswith('*'):
      if message.content.startswith('*hi'):
        await message.channel.send('Hello! Use /help, /cmds, or /about to learn more about me! ')

Token = os.environ['Token']
client.run(Token)

