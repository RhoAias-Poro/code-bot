import os
import discord
from discord.ext import commands
import requests  # send request through https to get the data from the api and return json
import json, datetime, asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/",
                   intents=intents)  #set prefix to use command


@bot.command(name="hi")  # if user enter /hi then print out hello
async def SendMessage(ctx):
  await ctx.send('Hello!')


@bot.command(name="pussy")
async def Cat(ctx):
  api = os.environ['API']
  # send requests to the api and response now a json
  response = requests.get(api)
  image_link = response.json()[0]  # like a list and need to choose index
  await ctx.send(image_link["url"])  # print the url


async def five_minutes_images():
  while True:
    now = datetime.datetime.now()
    then = now + datetime.timedelta(minutes=5)
    wait_time = (then - now).total_seconds()
    await asyncio.sleep(wait_time)

    ID = os.environ['channelID']  # return string obj
    channel = bot.get_channel(int(ID))
    await Cat(channel)


@bot.event
async def on_ready():  # event call when the bot is ready to use
  print(f"Logged in as : {bot.user.name}")
  await five_minutes_images()


pwd = os.environ['TOKEN']
bot.run(pwd)
