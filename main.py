import os
import discord
from discord.ext import commands
import requests  # send request through https to get the data from the api and return json
import json, datetime, asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.command(name="hi")
async def SendMessage(ctx):
  await ctx.send('Hello!')


@bot.command(name="pussy")
async def Cat(ctx):
  response = requests.get(  # send requests to the api and response now a json
    "https://api.thecatapi.com/v1/images/search?api_key=live_RbZGAHDXr6v3pV32pvbUe9yBEG6hH20VEtuJyDX0SsFJe3nVesTP00Z8ZLtrHlgz"
  )
  image_link = response.json()[0]  # like a list and need to choose index
  await ctx.send(image_link["url"])  # print the url


async def five_minutes_images():
  while True:
    now = datetime.datetime.now()
    then = now + datetime.timedelta(minutes=5)
    wait_time = (then - now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = bot.get_channel(1027525240055676969)
    await Cat(channel)


@bot.event
async def on_ready():  # event call when the bot is ready to use
  print(f"Logged in as : {bot.user.name}")
  await five_minutes_images()


pwd = os.environ['TOKEN']
bot.run(pwd)
