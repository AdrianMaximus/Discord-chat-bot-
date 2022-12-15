#main.py
import discord
from keep_alive import keep_alive 
from discord.ext import commands
import os
import openai
 
#make sure you have import all the above
 
bot = commands.Bot(
  command_prefix='?', #any prefix you want
  case_insensitive=False,
  description=None,
  intents=discord.Intents.all(), #enable intents in discord developer portal
  help_command=None
)
 
@bot.command()
async def test(ctx,*,arg): # * is used to make sure your complete arguement is used rather than first word
 
  response = openai.Completion.create(
    api_key = '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', #put your own api key here, mine doesnt work i deleted mine 🤣
    model="text-davinci-003",
    prompt=f"Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\nYou:{arg}\nMarv:",
    temperature=0.5,
    max_tokens=60,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0.0
  )
  await ctx.channel.send(response)
 
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"Hi"))
  print(f"Logged in as {bot.user.name}")
 
keep_alive()
 
 
bot.run(os.environ['BOT KEY']) #create a secret token named BOT KEY and paste ur token
