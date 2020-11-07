import os
from keep_alive import keep_alive
from discord.ext import commands
import discord
from time import sleep
from commands import clear
from eventcommands import eventcommands
import random

client = discord.Client() # Loades every extension.
@client.event
async def on_ready():
    clear()
    sleep(1)
    print("I'm online")
    sleep(1)
    print(f"username: {client.user.name}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you float"))
@client.event
async def on_message(message):
  balloon = "balloon"
  
  stranger = random.randint(1, 30)
  print(stranger)
  if (not message.author.id == 771891211287134219) and (not message.author.id == 464964930068807701) and (not message.author.id == 531221590147334184):
    if (balloon in message.content) or (":balloon:" in message.content):
   
      await message.channel.send(f"you look so tasty {message.author.name}")
    if stranger == 1:
      await message.channel.send(f"you want a balloon {message.author.name}?")
      await message.channel.send(":balloon:")
    if stranger == 2:
      await message.author.send(f"come dance with me {message.author.name}")
      await message.author.send("https://media1.tenor.com/images/c9e6aae474aebc3791e4463b4e116347/tenor.gif?itemid=15053394")
      await message.channel.send(":balloon:")
    if stranger == 3:
      await message.author.send("Ill be waiting")
      await message.author.send("https://tenor.com/view/it-2017-beverly-marsh-pennywise-youll-gif-9817323")
      sleep(10)
      await message.author.send("Actully my schedule is busy today how about another time?")
    if stranger == 4:
      await message.author.send("I just got my braces off! How do I look?")
      await message.author.send("https://tenor.com/view/pennywise-it-scary-smile-gif-12240248")
    if stranger == 5:
      await message.author.send("Hey there friend!")
      await message.author.send("https://tenor.com/view/it-pennywise-hello-wave-greetings-gif-14043524")
    if stranger == 6:
      await message.author.send("After thinking sbout what might scare you the most I have come to the decision that the next message you send may spam @everyone infinitly\nchoose your next words wisley friend my tasty tasty friend")
      sleep(60)
      await message.channel.send(f"I can think of {random.randint(10, 10000000)} diferent ways to devour you")
      await message.author.send("https://tenor.com/view/it-pennywise-happy-halloween-gif-15446356")
    if "hello" in message.content:
      await message.author.send("https://tenor.com/view/it-pennywise-hello-wave-greetings-gif-14043524")
      await message.channel.send(f"I can think of {random.randint(10, 10000000)} diferent ways to eat you")
    
      
    
      
  if message.content in eventcommands:
    await message.channel.send(eventcommands[message.content])
  if message.content == "test":
    channel = message.author.voice.channel
    await channel.connect()

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
client.run(token)  # Starts the bot