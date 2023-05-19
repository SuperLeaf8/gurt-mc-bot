import discord
import os
from dotenv import load_dotenv
Token = os.getenv("Token")
from discord.ext import commands

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

bot.run(Token)