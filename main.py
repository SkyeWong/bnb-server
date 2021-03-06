import os
import nextcord
import random
from nextcord.ext import commands
from nextcord import Embed, Interaction

TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix='-', case_insensitive=True, activity=nextcord.Game(name='-help'), owner_ids={806334528230129695, 706126877668147272})
embed_colours = [0x0071ad, 0x0064a4, 0x007dbd, 0x0096d6, 0x19afef, 0x32c8ff]


def roundup(number, round_to):
    return number if number % round_to == 0 else number + round_to - number % round_to


def rounddown(number, round_to):
    return number if number % round_to == 0 else number - number % round_to

for filename in os.listdir(f"cogs"):
    if filename.endswith("py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")
                    
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to nextcord!")
    print("Connected servers/guilds:")
    for guild in bot.guilds:
        print(f"  -{guild.name}(id={guild.id})")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return

def cd_embed(ctx, error):
    cd_ui = Embed()
    cd_ui.title = "Woah, chill."
    time = {
        "d": 0, 
        "h": 0,
        "m": 0,
        "s": round(error.retry_after)
    }
    while time["s"] >= 60:
        time["m"] += 1
        time["s"] -= 60
    while time["m"] > 60:
        time["h"] += 1
        time["m"] -= 60
    while time["h"] > 24:
        time["d"] += 1
        time["h"] -= 24
    time_txt = ""
    for i in time:
        if time[i] != 0:
            time_txt += f"{time[i]}{i} "
    cd_ui.description = f"Wait **{time_txt}** before using `{ctx.clean_prefix}{ctx.command.qualified_name}` again."
    cd_ui.colour = random.choice(embed_colours)
    return cd_ui

@bot.event
async def on_command_error(ctx: commands.Context, error):
    code_error = False
    if isinstance(error, commands.errors.CheckFailure):
        if ctx.command.cog_name == "Dev Only":
            await ctx.send("Only devs can use this command.\nOn the plus side, maybe this will be introduced to the game later!", delete_after=3)
        elif ctx.command.cog_name == "BNB Only":
            if ctx.guild.id != 827537903634612235:
                await ctx.send(content="This command is only available in the BNB server.", delete_after=3)
            elif ctx.channel.id != 836212817711333426:
                await ctx.send(content="This command is only available in <#836212817711333426>.", delete_after=3)
            else:
                await ctx.send(content="This command is only available to mods.", delete_after=3)
        else:
            await ctx.send("You are missing the role(s)/permission(s) to use this command.", delete_after=3)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=cd_embed(ctx, error), delete_after=3)
    else:
        code_error = True
        raise error
    if not code_error:
        try:
            await ctx.message.delete()
        except(nextcord.HTTPException):
            ctx.guild.owner.send(f"I don't have the correct perms in your server! Try checking my profile and re-add me to your server.\n`Server` - `{ctx.guild.name}`")

@bot.event
async def on_application_command_error(interaction: Interaction, error):
    if isinstance(error, commands.CommandOnCooldown):
        await interaction.response.send_message(embed=cd_embed(interaction, error), ephemeral=True)
    else:
        raise error

bot.run(TOKEN)
