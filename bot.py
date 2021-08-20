import os
import requests
import bs4
import discord
import random
import datetime
from fuzzywuzzy import fuzz
import yfinance as yf
from dotenv import load_dotenv
from discord.ext import commands

TOKEN = 'ODA2NjQ3MDQxMDMxNzk4Nzg1.YBsemQ.Wz3QzFbSNIf5pDIXvC-ME7Oujl4'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='meme', help='Provides user with an epic meme')
async def meme(ctx):
    x = random.randint(1,10)
    if x == 1:
        embed = discord.Embed()
        embed.description = "[Here's a random meme](https://cutt.ly/2kRQZOv)."
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed()
        embed.description = "[Here's a random meme](https://cutt.ly/lkQ8B3n)."
        await ctx.channel.send(embed=embed)
    
@bot.command(name='hentai', help='Provides user with a cool hentai gif')
async def hentai(ctx):
    x = random.randint(1,10)
    if x == 1:
        embed = discord.Embed()
        embed.description = "[Here's a random hentai gif](https://cutt.ly/2kRQZOv)."
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed()
        embed.description = "[Here's a random hentai gif](https://cutt.ly/lkQ8B3n)."
        await ctx.channel.send(embed=embed)

@bot.command(name='anime', help='Provides user with a rad anime gif')
async def anime(ctx):
    x = random.randint(1,10)
    if x == 1:
        embed = discord.Embed()
        embed.description = "[Here's a random anime gif](https://cutt.ly/2kRQZOv)."
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed()
        embed.description = "[Here's a random anime gif](https://cutt.ly/lkQ8B3n)."
        await ctx.channel.send(embed=embed)

@bot.command(name='cute', help='Will send a cute anime girl your way')
async def ecchi(ctx):
    path = r"C:\Users\tdayt\Desktop\aaa\Anime Collection"
    files=os.listdir(path)
    d=random.choice(files)
    real_path = r"/Users/tdayt/Desktop/aaa/Anime Collection/" + d
    await ctx.channel.send(file=discord.File(real_path))
    


@bot.command(name='stock', help='Gives current price of given stock')
async def stock(ctx, arg):

    stock_name = arg
    
    super_stock_name = stock_name.upper() # capitalizing stock name

    url = "https://finance.yahoo.com/quote/"

    full_url = url + stock_name

    response = requests.get(full_url).content

    soup = bs4.BeautifulSoup(response, 'html.parser')

    request = requests.get(full_url)
    if request.url != full_url:
        await ctx.channel.send(f"Couldn't find {super_stock_name} in database. Maybe learn how to spell?")
        return


    stock_price = soup.findAll(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")[0].text

    if stock_price == '':
        await ctx.channel.send(f"Couldn't find {super_stock_name} in database. Maybe learn how to spell?")
        return

    now = datetime.datetime.now()

    if (now.hour >= 16) or (now.hour < 9) or (now.hour == 9 and now.minute < 30):
        await ctx.channel.send(f"The market price for {super_stock_name} was ${stock_price} at closing hours.")
    else:
        await ctx.channel.send(f"The market price for {super_stock_name} is currently ${stock_price}.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msgAuthor = message.author

    if fuzz.token_set_ratio('based',message.content) > 70:
        await message.channel.send('Hey {}!'.format(message.author.mention) + ' Based on what?')

    elif 'b a s e d' in message.content:
        await message.channel.send('Hey {}!'.format(message.author.mention) + ' Based on what?')
    await bot.process_commands(message)

bot.run(TOKEN)