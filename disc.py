import requests
from discord import Embed, Colour

from data import config as c
from utils.loader import dbot, hooks

dbot.remove_command('help')


@dbot.command()
async def test(ctx):
    print(hooks.all_hooks())


@dbot.command()
async def armor(ctx):
    channel_id = ctx.message.guild.id
    webhook = await ctx.channel.create_webhook(name="Armor News",
                                               avatar=requests.get(
                                                   "https://i.comss.pics/2021/11/19/photo_2021-09-22_01-20-48.jpg"
                                               ).content,
                                               reason="Subscribe 'Project Armor' news")
    embed = Embed(title="✅ Успех!",
                  description="Новости будут приходить в этот канал.",
                  timestamp=ctx.message.created_at)
    embed.set_author(name="Project: Armor",
                     icon_url="https://i.comss.pics/2021/11/19/photo_2021-09-22_01-20-48.jpg",
                     url="https://t.me/projectarmor")
    await ctx.channel.send(embed=embed)
    hooks.add_hook(id=channel_id, link=webhook.url)


@dbot.command()
async def unarmor(ctx):
    channel_id = ctx.message.guild.id
    hooks.delete_hook(id=channel_id)


@dbot.command()
async def help(ctx):
    text = "Это новостная лента от **«Project: Armor»**\n" \
           "Отправь команду **!armor** в текстовый канал, где хочешь получать новости!\n"\
           "Чтобы отписаться от рассылки, напиши **!unarmor**"
    embed = Embed(title="👀 Привет!",
                  description=text,
                  color=Colour.gold()
                  )
    embed.set_thumbnail(url="https://i.comss.pics/2021/11/19/photo_2021-09-22_01-20-48.jpg")
    embed.set_author(name="Cillum Project",
                     icon_url="https://i.comss.pics/2021/11/13/CillumLogo2f869011530d4a42.png",
                     url="https://t.me/realnikonoff")
    await ctx.channel.send(embed=embed)


if __name__ == "__main__":
    print("Discord reg bot")
    dbot.run(c.DS_TOKEN)

# access =
# https://discordapp.com/oauth2/authorize?client_id=911300377591304313&scope=bot&permissions=536889344
