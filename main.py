import discord
import goon_client
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()
db = "/media/pi-nas/discordbot_data/discord.db"
client = goon_client.GoonClient(intents=discord.Intents.all(), db=db)
client.run(os.getenv("DISCORD_TOKEN"))
