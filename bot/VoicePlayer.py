from discord.ext import commands
import asyncio
import os


class VoicePlayer:

    def __init__(self, bot):
        self.VOLUME = 0.1
        self.bot = bot
        self.bot_DIR = '/home/pi/Bot/Botama_v3/bot/'
        self.SONG_DIR = self.bot_DIR + 'song/'
        self.SLEEP = 2

    # Command that allow you to play a song downloaded from Youtube
    # To make it work type !play ARandomYoutubeUrl
    @commands.command(name='yt', description='Play a song from a given YouTube link', pass_context=True)
    async def playYoutube(self, context, url):
        await self.play_a_song(context, url, yt=True)

    @commands.command(name='vlad', description='Play vladimir Cauchemard', pass_context=True)
    async def vlad(self, context):
        await self.play_a_song(context, 'vlad.mp3')

    @commands.command(name='cowboy', description='Screaming Cowboy', pass_context=True)
    async def cowboy(self, context):
        await self.play_a_song(context, 'screaming_cowboy.mp3')

    @commands.command(name='song', description='Play song from local dir', pass_context=True)
    async def song(self, context, song_name):
        if '.' in song_name:
            await self.play_a_song(context, song_name)
        else:
            await self.play_a_song(context, song_name + '.mp3')

    @commands.command(name='listSong', description='Show all song availables')
    async def listSong(self):
        files = [f for f in os.listdir(self.SONG_DIR)]
        files = '\n'.join(files)
        print(files)
        await self.bot.say('List of songs :\n{}'.format(files))

    # Make the self.bot leave the channel cause fuck it
    @commands.command(pass_context=True)
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

    async def play_a_song(self, context, song, yt=False):
        # grab the user who sent the command and his channel
        connected = await self.is_connected_to_voice_channel(context.message.server)
        if connected:
            return

        user = context.message.author
        voice_channel = user.voice.voice_channel
        channel = None
        # If the user is in a voice channel connect to this channel
        if voice_channel:
            channel = voice_channel.name
            # self.bot will say in what channel he's connecting
            await self.bot.say('User is in channel: ' + channel)
            # create StreamPlayer
            voice = await self.bot.join_voice_channel(voice_channel)
            if yt:
                player = await voice.create_ytdl_player(song)
            else :
                player = voice.create_ffmpeg_player(self.SONG_DIR + song)
            # We set the volume to 0.1 (1 is 100%, 2 for 200%, so 0.1 will be 10%)
            player.volume = self.VOLUME
            await asyncio.sleep(self.SLEEP)
            player.start()
            # While the song isn't finished, sleep(1) in order to avoid it closing before the end
            while not player.is_done():
                await asyncio.sleep(self.SLEEP)
            player.stop()
            await voice.disconnect()
        else:
            # Otherway the user isn't connected to a channel so but can't join obviously
            await self.bot.say('User is not in a channel.')


def setup(bot):
    bot.add_cog(VoicePlayer(bot))
