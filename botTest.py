import discord
import os
import asyncio
from discord.ext import commands
from discord import app_commands
import random
import yaml
from typing import Optional, List, Tuple


intents = discord.Intents.default()


bot = commands.Bot(command_prefix = '/', intents = intents)
valMentions = 0
@bot.event
async def on_ready():
    print("The bot is now updated and ready for use")
    print('----------------------------------------')

@bot.command()
async def valCount(ctx):
    await ctx.send(valMentions)
    print("bogoda")

@bot.command()
async def remove_random(ctx):
    voice_channel = await retrieve_active_voice_channel()
    while True:
        member_to_kick: Optional[discord.Member] = None
        random.shuffle(targeted_victims)
        for victim_user_id, percentage in targeted_victims:
            if voice_channel.guild.get_member(victim_user_id) not in voice_channel.members:
                continue
            random_int = random.randint(0,101)

            if random_int <= percentage * 100:
                member_to_kick = voice_channel.guild.get_member(victim_user_id)
                print("member found from victim list")

        if not member_to_kick:
            print("slecting member to kick")
            member_to_kick: discord.Member = random.choice(voice_channel.members)

    print("kicking member '%s'..." % (member_to_kick,))
    await member_to_kick.edit(voice_channel=None)
    
async def retrieve_active_voice_channel():
    """Scans all active voice channels the bot can see and returns a random one"""
    # Get all channels the bot can see
    channels = [c for c in bot.get_all_channels()]

    # Randomize them so we don't pick the same channel every time
    random.shuffle(channels)

    # Check if each channel is a VoiceChannel with active members
    for channel in channels:
        if isinstance(channel, discord.VoiceChannel):
            if len(channel.members) > 0:
                # We found an active voice channel!
                return channel

with open("config.yaml") as f:
    config = yaml.safe_load(f.read())
         
targeted_victims: List[Tuple[int, float]] = config.get("targeted_victims", [])




bot.run('')
