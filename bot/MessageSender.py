from discord.ext import commands
import os


class MessageSender:

    def __init__(self, bot):
        self.bot = bot
        self.bot_DIR = '/home/pi/Bot/Botama_v3/bot/'
        self.GIF_DIR = self.bot_DIR + 'gif/'
        self.MEDIA_DIR = self.bot_DIR + 'other/'


    @commands.command(name='yesn', description='Yeeeees nigga', pass_context=True)
    async def yesNigga(self, ctx):
        channel = ctx.message.channel
        file = self.GIF_DIR + 'yes_nigga.gif'
        with open(file, 'rb') as gif:
            await self.bot.send_file(channel, gif)


    @commands.command(name='gif', description='Send gif', pass_context=True)
    async def sendGif(self, ctx, gifName):
        channel = ctx.message.channel
        if ('.gif' in gifName):
            file = self.GIF_DIR + gifName
        else:
            file = self.GIF_DIR + gifName + '.gif'
        with open(file, 'rb') as gif:
            await self.bot.send_file(channel, gif)


    @commands.command(name='media', description='Send smtg from disk', pass_context=True)
    async def sendMedia(self, ctx, mediaName):
        channel = ctx.message.channel
        file = self.MEDIA_DIR + mediaName
        with open(file, 'rb') as f:
            await self.bot.send_file(channel, f)


    @commands.command(name='listGif', description='Show all song availables')
    async def listGif(self):
        files = [f for f in os.listdir(self.GIF_DIR)]
        files = '\n'.join(files)
        print(files)
        await self.bot.say('List of gif :\n{}'.format(files))


    @commands.command(name='listMedia', description='Show all other media availables')
    async def listMedia(self):
        files = [f for f in os.listdir(self.MEDIA_DIR)]
        files = '\n'.join(files)
        print(files)
        await self.bot.say('List of gif :\n{}'.format(files))





def setup(bot):
    bot.add_cog(MessageSender(bot))

