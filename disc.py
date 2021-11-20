import aiohttp
import requests

from data import config as c

from discord.ext import commands
from discord import Embed, Colour, Webhook, AsyncWebhookAdapter
from utils.loader import dbot, hooks

from utils import logger


help_text = "Это бот с новостной лентой от **«Project: Armor»**\n"\
            "Отправь команду `!armor` в текстовый канал, где хочешь получать новости!\n"\
            "Чтобы отписаться от рассылки, напиши `!unarmor`\n\n"\
            "_На одном сервере можно подключить только один канал. "\
            "При повторной команде канал будет перепривязан..._"

pa_url = "https://i.comss.pics/2021/11/19/photo_2021-09-22_01-20-48.jpg"

dbot.remove_command('help')


@dbot.command()
@commands.has_guild_permissions(administrator=True)
async def armor(ctx):
    try:
        channel_id = ctx.message.guild.id
        if hooks.get_hook(id=channel_id) is not None:
            logger.logging.debug("The hook exists")
            async with aiohttp.ClientSession() as session:
                old_hook = Webhook.from_url(url=hooks.get_hook(id=channel_id)[0], adapter=AsyncWebhookAdapter(session))
                await old_hook.delete()
                hooks.delete_hook(id=channel_id)
                logger.logging.debug("The hook deleted")

        try:
            name = "Project: Armor"
            icon_url = pa_url
            url = "https://t.me/projectarmor"
            color = Colour.dark_green()

            title = "✅ Рассылка подключена!"
            description = "Новости от **«Project: Armor»** будут приходить в этот канал.\n\n" \
                          "_Чтобы отписаться от рассылки, напишите `!unarmor`_"
            logger.logging.debug("Webhook created")

            webhook = await ctx.channel.create_webhook(name="Armor News",
                                                       avatar=requests.get(pa_url).content,
                                                       reason="Subscribe 'Project Armor' news")
            hooks.add_hook(id=channel_id, link=webhook.url)
            logger.logging.info("Webhook inserted")

        except Exception as e:
            logger.logging.warning(e)
            name = "Cillum Project"
            title = "❌ Ошибка получения вебхука!"
            description = "Проверьте права бота и попробуйте снова.\n\n" \
                          "Если ошибка повторяется, обратитесь в [администратору](https://t.me/KoshkenS)."
            color = Colour.dark_red()
            icon_url = "https://i.comss.pics/2021/11/13/CillumLogo2f869011530d4a42.png"
            url = "https://t.me/cillum_project"

        e = Embed(title=title,
                  description=description,
                  color=color,
                  timestamp=ctx.message.created_at)
        e.set_author(name=name,
                     icon_url=icon_url,
                     url=url)
        await ctx.channel.send(embed=e)

    except Exception as e:
        logger.logging.error(e)


@commands.has_guild_permissions(administrator=True)
@dbot.command()
async def unarmor(ctx):
    try:
        channel_id = ctx.message.guild.id

        if hooks.get_hook(id=channel_id) is not None:
            async with aiohttp.ClientSession() as session:
                old_hook = Webhook.from_url(url=hooks.get_hook(id=channel_id)[0], adapter=AsyncWebhookAdapter(session))
                await old_hook.delete()
                hooks.delete_hook(id=channel_id)

            title = "❎ Рассылка отключена!"
            description = "Новости от **«Project: Armor»** больше не будут приходить в этот канал.\n\n" \
                          "_Чтобы снова подписаться на рассылку, напишите `!armor`_"
            color = Colour.dark_green()

        else:
            title = "❌ ༼ つ ◕_◕ ༽つУже удалён༼ つ ◕_◕ ༽つ"
            description = "Рассылка не подключена, вебхука не существует.\n\n" \
                          "_Напишите `!help` для помощи или `!armor` для подключения рассылки._"
            color = Colour.dark_red()

        e = Embed(title=title,
                  description=description,
                  color=color,
                  timestamp=ctx.message.created_at)
        e.set_author(name="Project: Armor",
                     icon_url=pa_url,
                     url="https://t.me/projectarmor")

        await ctx.channel.send(embed=e)

    except Exception as e:
        logger.logging.error(e)


@dbot.command()
async def help(ctx):
    try:
        e = Embed(title="👀 Привет!",
                  description=help_text,
                  color=Colour.from_rgb(0, 199, 255))
        e.set_thumbnail(url=pa_url)
        e.set_author(name="Cillum Project",
                     icon_url="https://i.comss.pics/2021/11/13/CillumLogo2f869011530d4a42.png",
                     url="https://t.me/cillum_project")
        await ctx.channel.send(embed=e)
    except Exception as e:
        logger.logging.error(e)


@dbot.event
async def on_guild_join(guild):
    e = Embed(title="👀 Привет!",
              description=help_text,
              color=Colour.from_rgb(0, 199, 255))
    e.set_thumbnail(url=pa_url)
    e.set_author(name="Cillum Project",
                 icon_url="https://i.comss.pics/2021/11/13/CillumLogo2f869011530d4a42.png",
                 url="https://t.me/cillum_project")
    if guild.system_channel is not None:
        await guild.system_channel.send(embed=e)
    else:
        logger.logging.info(f"No system channel at «{guild}/{guild.id}» server")


if __name__ == "__main__":
    print(c.DS_INVITE_LINK)
    dbot.run(c.DS_TOKEN)
