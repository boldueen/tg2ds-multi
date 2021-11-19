import discord
import configparser
from discord.ext import commands

conf = configparser.ConfigParser()
conf.read('config.ini')


client = discord.Client()

bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)
async def getguild(ctx):
    id = ctx.message.guild.id
    print(message.channel.id)
    await ctx.send(id)

@bot.command()
async def send(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def news(ctx, channel_id, text):
    emb = discord.Embed(title='Новость!!!', timestamp=ctx.message.created_at)
    channel = bot.get_channel(channel_id)
    await ctx.channel.send(embed=emb)












bot.run(conf['DS']['BOT'])