import discord
import os
from dotenv import load_dotenv
Token = os.getenv("Token")
from discord.ext import commands
import requests

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("i am alive")

@bot.command()
async def hello(ctx):
    username = ctx.message.author.mention
    await ctx.send("Hello there " + username)

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

bot.run(Token)