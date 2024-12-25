import discord
import random
import os
import subprocess
import sys
from discord.ext import commands
from dotenv import load_dotenv

# List required packages
required_packages = ["discord.py", "python-dotenv"]

for package in required_packages:
    try:
        __import__(package.split('.')[0])  # Import the base module
    except ImportError:
        print(f"Package {package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True  # Enable message intents
intents.message_content = True  # Allow content analysis
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    # Ignore bot's own messages to avoid infinite loops
    if message.author == bot.user:
        return

    # Check if the message contains attachments (e.g., images)
    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type and "image" in attachment.content_type:
                image = True
        if image == True:
            if random.randint(1, 50) == 1:
                await message.reply("Wish someone would do this to me", mention_author=True)

    # Else check for a 1/100 chance
    else:    
        if random.randint(1, 100) == 1:
            emojiChance = random.randint(0,5)
            emojis = [":gort:", ":gort:", ":yawn:", ":coma:", ":HUH:" ,":Salami:"]
            await message.channel.send(emojis[emojiChance])

    # Allow other commands to still work
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def tanistanis(ctx):
    await ctx.send(":smile:")

bot.run(TOKEN)
