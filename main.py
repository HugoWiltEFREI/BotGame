import os
import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables from .env
load_dotenv()

# Retrieve the bot token from the .env file
TOKEN = os.getenv("DISCORD_TOKEN")

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True  # To read the content of messages
bot = commands.Bot(command_prefix="!", intents=intents)

# Function to send a daily message with an image
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    scheduler = AsyncIOScheduler()
    # Schedule a daily ping at 18:40
    scheduler.add_job(send_daily_message_with_image, 'cron', hour=18, minute=40)
    scheduler.start()

async def send_daily_message_with_image():
    guild_id = 1324751399245844571  # Replace with your server's ID
    channel_id = 1324784559904133170  # Replace with the channel's ID
    role_id = 1324752392926789642  # Replace with the role's ID

    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)
    role = guild.get_role(role_id)

    if channel and role:
        await channel.send(
            f"{role.mention} 5 minutes avant l'escorte de guilde, n'oubliez pas de monter et de faire votre rassemblement ! 🎉",
            file=discord.File("cheval event.jpg")
        )

# Command to manually test sending images
@bot.command()
async def test_image(ctx):
    # Local image
    await ctx.send("Image locale :", file=discord.File("cheval event.jpg"))

# Run the bot using the token
if TOKEN:
    bot.run(TOKEN)
else:
    print("Bot token not found. Please set it in the .env file.")
