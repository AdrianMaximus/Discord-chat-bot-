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
  query = ctx.message.content
  response = openai.Completion.create(
    api_key = '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', #put your own api key here, mine doesnt work i deleted mine 🤣
    model="text-davinci-003",
    prompt=query,
    temperature=0.5,
    max_tokens=60,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0.0
  )
  await ctx.channel.send(content=response['choices'][0]['text'].replace(str(query), ""))
 
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"Hi"))
  print(f"Logged in as {bot.user.name}")
 
keep_alive()
 
 
bot.run(os.environ['BOT KEY']) #create a secret token named BOT KEY and paste ur token
