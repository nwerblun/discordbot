import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

env_file = open(".env")
env = env_file.readlines()
env_file.close()
# 0 = app id, 1 = login token, 2 = public key
token = env[1].replace("DISCORD_TOKEN=", "").strip()


@client.event
async def on_message(message):
    if message.content.startswith("$test"):
        await message.channel.send("sup")

client.run(token)
