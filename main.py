import discord
import os
import json
from discord.ext import commands
import requests


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("i am alive")

@bot.command()
async def hello(ctx):
    username = ctx.message.author.mention
    await ctx.send("Hello there " + username)
 
# minecraft server get
@bot.command()
async def minecraft(ctx):
    r = requests.get('https://api.mcsrvstat.us/2/gurt.cc')
    json_data = r.json()
    online = str(json_data["online"])
    playerCount = str(json_data["players"]["online"])
    version = str(json_data["version"])
    hostname = json_data["hostname"]

    embed = discord.Embed(
        title="Server Info",
        description='Online: ' + online + '\nonline: ' + playerCount + '\nHostname: ' + hostname + '\nVersion: ' + version,
        color=discord.Colour.dark_gray()
    )

    await ctx.send(embed=embed)

with open("token.json","r") as f:
    token = json.load(f)

bot.run(token)