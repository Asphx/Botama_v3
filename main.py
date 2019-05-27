import discord
from discord.ext import commands

with open('/home/ubuntu/Workspace/Botama_v3/key', 'r') as f:
    TOKEN=f.readline()
description ='''Bot Serveur Saitama'''
bot = commands.Bot(command_prefix=('!','?'), description=description)

bot.load_extension('bot.VoicePlayer')
bot.load_extension('bot.MessageSender')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

bot.run(TOKEN.strip())
