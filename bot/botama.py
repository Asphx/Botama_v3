import discord
from discord.ext import commands
import asyncio


TOKEN = 'NTIxMjM2NzE3NTE3Mjc1MTQy.Dxz_6A.49eva4xSJ0Cq1T-k1-OCSJFIBIk'
description ='''Bot Serveur Saitama'''

bot = commands.Bot(command_prefix='!', description=description)
client = discord.Client()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')


@bot.command(name='song', description='Play a song', pass_context=True)
async def playSong(context, url):
    # grab the user who sent the command
    user = context.message.author
    voice_channel = user.voice.voice_channel
    channel = None
    if voice_channel!= None:
        channel = voice_channel.name
        await bot.say('User is in channel: '+ channel)
        # create StreamPlayer
        voice = await bot.join_voice_channel(voice_channel)
        player = await voice.create_ytdl_player(url)
        player.volume = 0.1
        player.start()
        
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await voice.disconnect()
    else:
        await bot.say('User is not in a channel.')

@bot.command(name='vlad', description='Play a song', pass_context=True)
async def playVlad(context):
    for x in client.voice_clients:
        if x.server == context.message.server:
            return await x.disconnect()

    # grab the user who sent the command
    user = context.message.author
    voice_channel = user.voice.voice_channel
    channel = None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel = voice_channel.name
        await bot.say('User is in channel: '+ channel)
        # create StreamPlayer
        voice = await bot.join_voice_channel(voice_channel)
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=hpjV962DLWs')
        player.volume = 0.1
        player.start()
        
        while not player.is_done():
            await asyncio.sleep(1)
        player.stop()
        await voice.disconnect()
    else:
        await bot.say('User is not in a channel.')


@bot.command(pass_context=True)
async def leave(context):
    server = context.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

bot.run(TOKEN)

