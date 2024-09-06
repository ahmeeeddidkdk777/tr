import os
import discord
from discord.ext import commands
import asyncio

# قراءة التوكن من المتغير البيئي
TOKEN = os.getenv('DISCORD_TOKEN')

# إعداد البوت مع البريفكس الذي تريده
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def send_numbers(ctx):
    for i in range(1, 101):
        await ctx.send(str(i))
        await asyncio.sleep(1)  # الانتظار لمدة ثانية بين الرسائل لتجنب تجاوز حد السرعة

bot.run(TOKEN)
