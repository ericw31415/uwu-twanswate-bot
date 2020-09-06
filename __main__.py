import discord
import os
from dotenv import load_dotenv

def uwuify(str):
    return str.replace("l", "w").replace("r", "w") + " uwu"

load_dotenv()
bot_token = os.getenv("DISCORD_BOT_TOKEN")

client = discord.Client()

@client.event
async def on_connect():
    print(f"Bot connected to Discord as user \"{client.user}\".")

@client.event
async def on_ready():
    print("Ready!")

@client.event
async def on_disconnect():
    print("Bot disconnected.")
    print("Attempting to reconnect...")

@client.event
async def on_message(msg):
    if msg.content == "uwu":
        await msg.channel.send(uwuify((
            await msg.channel.history(limit=1, before=msg.created_at).flatten()
        )[0].content))

print(f"Connecting to Discord...")
client.run(bot_token)
