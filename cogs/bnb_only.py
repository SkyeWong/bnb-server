import os
import nextcord
import random
from main import bot
from datetime import datetime
from nextcord.ext import commands
from nextcord import Embed, Interaction
from nextcord.ui import Button, View
from typing import Optional

class BnbOnly(commands.Cog, name="BNB Only"):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None 

    async def cog_check(self, ctx):
        # check if server is BNB
        return ctx.guild.id == 827537903634612235 
    
    def in_general_chat(ctx:commands.Context):
        return ctx.channel.id == 836212817711333426
    
    @commands.command(name="deadchat", help="LETS RETVIVE THE CHAT")
    @commands.cooldown(rate=1, per=1800, type=commands.BucketType.guild)
    @commands.check(in_general_chat)
    @commands.has_any_role(
        829931104995115039, #senior mod
        827548548454678548, #mod
        962604934820417616, #trial mod
        827553090848161802, #skye
        961646555226587268, #keith
        961646665167683644, #karson
        962011095009210468, #hoho
        966654522304897034  #ginny
    ) # The bnb staffs role
    async def deadchat(self, ctx: commands.Context, *, message: str="None"):
        try:
            await ctx.message.delete()
        except(nextcord.HTTPException):
            ctx.guild.owner.send(f"I don't have the correct perms in your server! Try checking my profile and re-add me to your server.\n`Server` - `{ctx.guild.name}`")
        embed = Embed()
        embed.set_author(name="・DEAD CHAT ALERT", icon_url="https://cdn.discordapp.com/emojis/966652439300300901.gif")
        embed.description = "<:deadchat:965893342695157780> " * 6 # dead chat emoji
        embed.add_field(name=f"LET'S REVIVE THE CHAT RN!", value=f"**{ctx.author.mention} has requested you guys to revive the chat!**", inline=False)
        embed.add_field(name="`Message:`", value=message, inline=False)
        await ctx.send(content="<@&965892736882462741>", embed=embed) # ping the @ chat revive role

    

def setup(bot: commands.Bot):
    bot.add_cog(BnbOnly(bot))