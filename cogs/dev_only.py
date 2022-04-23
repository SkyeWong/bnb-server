import nextcord
from datetime import datetime
from main import bot
import main
import random
from nextcord.ext import commands
from texttable import Texttable
import db

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

    @commands.command(name="texttable", brief="example of texttable module.")
    async def texttable(self, ctx):
        table = Texttable()
        table.set_cols_align(["l", "r", "c"])
        table.set_cols_valign(["t", "m", "b"])
        table.add_rows([["Name", "Age", "Nickname"],
                        ["Mr\nXavier\nHuon", 32, "Xav'"],
                        ["Mr\nBaptiste\nClement", 1, "Baby"],
                        ["Mme\nLouise\nBourgeau", 28, "Lou\n\nLoue"]])
        await ctx.send(f"```ml\n{table.draw()}```")
        await ctx.send("** **")
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_cols_dtype(['t',  # text
                              'f',  # float (decimal)
                              'e',  # float (exponent)
                              'i',  # integer
                              'a']) # automatic
        table.set_cols_align(["l", "r", "r", "r", "l"])
        table.add_rows([["text",    "float", "exp", "int", "auto"],
                        ["abcd",    "67",    654,   89,    128.001],
                        ["efghijk", 67.5434, .654,  89.6,  12800000000000000000000.00023],
                        ["lmn",     5e-78,   5e-78, 89.4,  .000000000000128],
                ["opqrstu", .023,    5e+78, 92.,   12800000000000000000000]])
        await ctx.send(f"```ml\n{table.draw()}```")
    
    @commands.command(name="usersview")
    async def usersview(self, ctx):
        await ctx.send('Fetching results...')
        sql = "SELECT * from users"
        cursor = db.execute(sql)
        for row in cursor.fetchall():
                await ctx.send(row)
        
def setup(bot: commands.Bot):
    bot.add_cog(dev_only(bot))
