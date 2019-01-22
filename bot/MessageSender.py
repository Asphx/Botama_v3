from discord.ext import commands
import os


class MessageSender:

    def __init__(self, bot):
        self.bot = bot
        self.bot_DIR = '/home/pi/Bot/Botama_v3/bot/'
        self.GIF_DIR = self.bot_DIR + 'gif/'

    @commands.command(name='yesn', description='Yeeeees nigga', pass_context=True)
    async def yesNigga(self, ctx):
        channel = ctx.message.channel
        file = self.GIF_DIR + 'yes_nigga.gif'
        with open(file, 'rb') as gif:
            await self.bot.send_file(channel, gif)


def setup(bot):
    bot.add_cog(MessageSender(bot))
