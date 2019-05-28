from discord.ext import commands
import os


class MessageSender:

    def __init__(self, bot):
        self.bot = bot
        self.bot_DIR = os.path.dirname(os.path.realpath(__file__))
        self.GIF_DIR = self.bot_DIR + 'gif/'
        self.MEDIA_DIR = self.bot_DIR + 'media/'
        self.SONG_DIR = self.bot_DIR + 'song/'



    @commands.command(name='yesn', description='Yeeeees nigga', pass_context=True)
    async def yes_nigga(self, ctx):
        path = self.GIF_DIR + 'yes_nigga.gif'
        await self.send_file(ctx, path)


    @commands.command(name='gif', description='Send gif', pass_context=True)
    async def send_gif(self, ctx, gifName):
        path = self.GIF_DIR + gifName
        await self.send_file(ctx, path)


    @commands.command(name='media', description='Send smtg from disk', pass_context=True)
    async def send_media(self, ctx, mediaName):
        path = self.MEDIA_DIR + mediaName
        await self.send_file(ctx, path)

    @commands.command(name='list_gif', description='Show all song availables')
    async def list_gif(self):
        await self.list_files(self.GIF_DIR)


    @commands.command(name='list_media', description='Show all other media availables')
    async def list_media(self):
        await self.list_files(self.MEDIA_DIR)

    @commands.command(name='list_song', description='Show all song availables', brief='List all local song')
    async def song_list(self):
        await self.list_files(self.SONG_DIR)


    async def list_files(self, dir):
        files = [f for f in os.listdir(dir)]
        files = '\n'.join(files)
        print(files)
        await self.bot.say('List of {} : \n{}'.format(dir.split('/')[-2], files))

    async def send_file(self, ctx, file_name):
        channel = ctx.message.channel
        file = file_name
        with open(file, 'rb') as f:
            await self.bot.send_file(channel, f)


def setup(bot):
    bot.add_cog(MessageSender(bot))
