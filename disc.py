import requests

from data import config as c

from discord import Embed, Colour
from utils.loader import dbot, hooks

from utils import logger

dbot.remove_command('help')


@dbot.command()
async def armor(ctx):
    channel_id = ctx.message.guild.id

    try:
        webhook = await ctx.channel.create_webhook(name="Armor News",
                                                   avatar=requests.get(
                                                       "https://i.comss.pics/2021/11/19/photo_2021-09-22_01-20-48.jpg"
                                                   ).content,
                                                   reason="Subscribe 'Project Armor' news")
        name = "Project: Armor"
        icon_url = "https://i.comss.pics/2021/11/19/photo_2021-09-22_01-20-48.jpg"
        url = "https://t.me/projectarmor"
        color = Colour.dark_green()

        if hooks.add_hook(id=channel_id, link=webhook.url):
            title = "✅ Рассылка подключена!"
            description = "Новости от **«Project: Armor»** будут приходить в этот канал.\n\n"\
                          "Чтобы отписаться от рассылки, напишите `!unarmor`"
        else:
            title = "✅ Рассылка подключена!"
            description = "Новости от **«Project: Armor»** теперь будут приходить в этот канал. " \
                          "Старая запись удалена.\n\n" \
                          "Чтобы отписаться от рассылки, напишите `!unarmor`"

    except Exception as e:
        logger.logging.warning(e)
        name = "Cillum Project"
        title = "❌ Ошибка получения вебхука!"
        description = "Боту не удалось создать вебхук для рассылки новостей. Проверьте его права и попробуйте снова.\n"\
                      "\nЕсли вы уверены, что права выдана, но ошибка повторяется, " \
                      "обратитесь в [поддержку](https://t.me/realnikonoff)."
        # TODO вставить ссылку на поддержку
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


@dbot.command()
async def unarmor(ctx):
    channel_id = ctx.message.guild.id

    if hooks.delete_hook(id=channel_id):
        title = "❎ Рассылка отключена!"
        description = "Новости от **«Project: Armor»** больше не будут приходить в этот канал.\n\n"\
                      "Чтобы снова подписаться на рассылку, напишите `!armor`"
        color = Colour.dark_green()
    else:
        title = "❌ Рассылка отключена!"
        description = "Рассылка уже отключена на этом сервере.\n" \
                      "Её можно включить командой `!armor`"
        color = Colour.dark_red()

    e = Embed(title=title,
              description=description,
              color=color,
              timestamp=ctx.message.created_at)
    e.set_author(name="Project: Armor",
                 icon_url="https://i.comss.pics/2021/11/19/photo_2021-09-22_01-20-48.jpg",
                 url="https://t.me/projectarmor")

    await ctx.channel.send(embed=e)


@dbot.command()
async def help(ctx):
    text = "Это бот с новостной лентой от **«Project: Armor»**\n" \
           "Отправь команду `!armor` в текстовый канал, где хочешь получать новости!\n"\
           "Чтобы отписаться от рассылки, напиши `!unarmor`\n\n" \
           "На одном сервере можно привязать только один канал. " \
           "При повторной команде канал будет перепривязан..."
    e = Embed(title="👀 Привет!",
              description=text,
              color=Colour.from_rgb(0, 199, 255))
    e.set_thumbnail(url="https://i.comss.pics/2021/11/19/photo_2021-09-22_01-20-48.jpg")
    e.set_author(name="Cillum Project",
                 icon_url="https://i.comss.pics/2021/11/13/CillumLogo2f869011530d4a42.png",
                 url="https://t.me/cillum_project")
    await ctx.channel.send(embed=e)


if __name__ == "__main__":
    dbot.run(c.DS_TOKEN)

# https://discordapp.com/oauth2/authorize?client_id=911300377591304313&scope=bot&permissions=536889344
