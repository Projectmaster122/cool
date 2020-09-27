import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("bot ready")

@client.command()
async def hi(ctx):
    await ctx.send("hi")

@client.run("token")