import nextcord
from datetime import datetime
from main import bot
import main
import random
from nextcord.ext import commands
from texttable import Texttable

class dev_only(commands.Cog, name='Tests Commands'):
    """Never care about them. Simple tests for complicated concepts."""
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command(name="invite", brief="Invite me!", help="Shows the invite link for this bot. Nothing more, nothing less.")
    async def invite(self, ctx):
        embed = nextcord.Embed()
        embed.title = "Invite me to your server and have some fun!"
        embed.set_author(name=bot.user.name, icon_url= bot.user.avatar)
        embed.description = "[here](https://discord.com/api/oauth2/authorize?client_id=906505022441918485&permissions=8&scope=bot)"
        embed.colour = random.choice(main.embed_colours)
        await ctx.send(embed=embed)
        
    @commands.command(name="whatsthetime", brief="Shows the time.")
    async def whatsthetime(self, ctx):
        await ctx.send(f"<t:{int(datetime.now().timestamp())}>")
        
def setup(bot: commands.Bot):
    bot.add_cog(dev_only(bot))
