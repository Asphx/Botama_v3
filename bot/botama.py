import discord
from discord.ext import commands
import asyncio


TOKEN = 'NTIxMjM2NzE3NTE3Mjc1MTQy.Dxz_6A.49eva4xSJ0Cq1T-k1-OCSJFIBIk'
description ='''Bot Serveur Saitama'''

bot = commands.Bot(command_prefix=('!','?'), description=description)


client = discord.Client()

# TODO: Create a global player volume variable in order to avoid typing over 9000 times the same fucking player.volume = !@#$ in every function that uses it

# Bot start : 
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')



# Command that allow you to play a song downloaded from Youtube
# To make it work type !play ARandomYoutubeUrl
@bot.command(name='play', description='Play a song from a given YouTube link', pass_context=True)
async def playSong(context, url):
    # grab the user who sent the command and his channel
    user = context.message.author
    voice_channel = user.voice.voice_channel
    channel = None
    # If the user is in a voice channel connect to this channel
    if voice_channel!= None:
        channel = voice_channel.name
        # Bot will say in what channel he's connecting
        await bot.say('User is in channel: '+ channel)
        # create StreamPlayer
        voice = await bot.join_voice_channel(voice_channel)
        player = await voice.create_ytdl_player(url)
        # We set the volume to 0.1 (1 is 100%, 2 for 200%, so 0.1 will be 10%)
        player.volume = 0.1
        player.start()
       # While the song isn't finished, sleep(1) in order to avoid it closing before the end (TBH it will close just after he loaded the song) 
        while not player.is_done():
            await asyncio.sleep(1)
        player.stop()
        await voice.disconnect()
    else:
        # Otherway the user isn't connected to a channel so but can't join obviously
        await bot.say('User is not in a channel.')


# Exact same commad the 'playSong' but it will play a song from OUR LORD 
# VLADIMIR CAUCHEMARD
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

# Make the bot leave the channel cause fuck it
@bot.command(pass_context=True)
async def leave(context):
    server = context.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

bot.run(TOKEN)

