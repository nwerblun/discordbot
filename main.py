import discord
import goon_client
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()
db = os.getenv("DATA_ROOT_DIR") + "discord.db"
client = goon_client.GoonClient(intents=discord.Intents.all(), db=db)
client.run(os.getenv("DISCORD_TOKEN"))
