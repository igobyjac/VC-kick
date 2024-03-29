import discord
import os
import asyncio
from discord.ext import commands
from discord import app_commands
import random
from typing import Optional, List, Tuple


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = '/', intents = intents)


@bot.event
async def on_ready():
    print("The bot is now updated and ready for use")
    print('----------------------------------------')

@bot.command()
async def botTest(ctx):
    await ctx.send(valMentions)
    await ctx.send("BOT WORKS")
    print("Test Complete")

@bot.command()
async def remove_random(interaction: discord.Interaction):
    users = [user for user in interaction.guild.members if not(user.bot or user == interaction.guild.owner or user.voice is None  or user.voice.mute == True)]

    if not users:
        await interaction.response.send_message("No users in voice channels")
        return
    
    chosen_user = random.choice(users)
    await asyncio.sleep(1)
    await chosen_user.move_to(None)
    print(f'{chosen_user} has been kicked')
        
    
bot.run('')
