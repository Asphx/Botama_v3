from discord.ext import commands
import asyncio
import os
import subprocess

class VoicePlayer:

    def __init__(self, bot):
        self.VOLUME = 0.1
        self.bot = bot
        self.bot_DIR = '/home/pi/Bot/Botama_v3/bot/'
        self.SONG_DIR = self.bot_DIR + 'song/'
        self.SLEEP = 1

    # Command that allow you to play a song downloaded from Youtube
    # To make it work type !play ARandomYoutubeUrl
    @commands.command(name='yt', description='Play a song from a given YouTube link', brief='Play a youtube song', pass_context=True)
    async def playYoutube(self, context, url):
        await self.play_yt_song(context, url)

    @commands.command(name='vlad', description='Play vladimir Cauchemard', brief='Play Vladimir Cauchemard song', pass_context=True)
    async def vlad(self, context):
        await self.play_local_song(context, 'vlad.mp3')

    @commands.command(name='cowboy', description='Screaming Cowboy', brief='Play Screaming Cowboy song', pass_context=True)
    async def cowboy(self, context):
        await self.play_local_song(context, 'screaming_cowboy.mp3')


    @commands.command(name='ez4ence', description='EZ4ENCE', brief='Play EZ4ENCE song', pass_context=True)
    async def cowboy(self, context):
        await self.play_local_song(context, 'ez4ence.mp3')
   
    @commands.command(name='song', description='Play song from local dir', brief='Play a song from local dir (use !songList)', pass_context=True)
    async def song(self, context, song_name):
        await self.play_local_song(context, song_name)

    # Make the self.bot leave the channel cause fuck it
    @commands.command(pass_context=True, brief='Make the bot leave vocal song', description='Make the bot leave vocal song')
    async def leave(self, context):
        server = context.message.server
        voice_client = self.bot.voice_client_in(server)
        await voice_client.disconnect()

    async def is_connected_to_voice_channel(self, server):
        if self.bot.is_voice_connected(server):
            await self.bot.say('Already connected to a vocal')
            return True
        else:
            return False

    async def play_yt_song(self, context, song):
        # grab the user who sent the command and his channel
        connected = await self.is_connected_to_voice_channel(context.message.server)
        if connected:
            return
        user = context.message.author
        voice_channel = user.voice.voice_channel
        # If the user is in a voice channel connect to this channel
        if voice_channel:
            channel = voice_channel.name
            # self.bot will say in what channel he's connecting
            await self.bot.say('User is in channel: ' + channel)
            # create StreamPlayer
            voice = await self.bot.join_voice_channel(voice_channel)
            player = await voice.create_ytdl_player(song)
            # We set the volume to 0.1 (1 is 100%, 2 for 200%, so 0.1 will be 10%)
            player.volume = self.VOLUME
            player.start()
            await asyncio.sleep(self.SLEEP)
            # While the song isn't finished, sleep(1) in order to avoid it closing before the end
            while not player.is_done() or player.is_playing():
                await asyncio.sleep(self.SLEEP)
            player.stop()
            await voice.disconnect()
        else:
            # Otherway the user isn't connected to a channel so but can't join obviously
            await self.bot.say('User is not in a channel.')


    async def play_local_song(self, context, song):
        connected = await self.is_connected_to_voice_channel(context.message.server)
        if connected:
            return
        user = context.message.author
        voice_channel = user.voice.voice_channel
        if voice_channel:
            channel = voice_channel.name
            await self.bot.say('User is in channel: ' + channel)
            voice = await self.bot.join_voice_channel(voice_channel)

            if "." in song:
                player = voice.create_ffmpeg_player(self.SONG_DIR + song)
            else :
                player = voice.create_ffmpeg_player(self.SONG_DIR + song + '.mp3')
            player.volume = self.VOLUME
            player.start()
            await asyncio.sleep(self.SLEEP)
            while not player.is_done() or player.is_playing():
                await asyncio.sleep(self.SLEEP)
            player.stop()
            await voice.disconnect()
        else:
            await self.bot.say('User is not in a channel.')


    @commands.command(name='dl-yt', description='Download a song from a given YouTube link into the server', brief='Download a youtube song', pass_context=True)
    async def download_local_song(self, context, song, name):
        user = context.message.author
        await self.bot.say('Start the download of {} giving it the name of {}.mp3'.format(song, name))
        p = subprocess.Popen(['/usr/bin/python3', '/home/pi/Bot/Botama_v3/bot/SysInteraction.py', 'dl-yt', song, name])

def setup(bot):
    bot.add_cog(VoicePlayer(bot))
