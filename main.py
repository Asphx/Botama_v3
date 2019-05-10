import discord
from discord.ext import commands
import bot.myToken as t

TOKEN = t.getKey()
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
    # Serveur : Saitama

bot.run(TOKEN)
