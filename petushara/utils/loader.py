from data import config as c
from aiogram import Bot, Dispatcher

from discord import Client
from discord.ext import commands

from data.database import Hooks

tbot = Bot(token=c.TG_TOKEN)
dp = Dispatcher(tbot)

client = Client()
dbot = commands.Bot(command_prefix='!')

hooks = Hooks()
hooks.create_table_hooks()


if __name__ == "__main__":
    print("Do not run this file. Use \033[94mdocker build .\033[0m at root of project")
