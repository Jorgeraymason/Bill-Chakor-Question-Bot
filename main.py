from discord.ext import commands
import discord

import os

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("$"),
    intents=discord.Intents.all()
)

@bot.event
async def on_ready():
    print("Bot is Ready!")

bot.run(os.getenv("TOKEN"))