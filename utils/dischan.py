import os

import aiohttp
from discord import Embed, Webhook, AsyncWebhookAdapter, Colour, File

from utils.loader import hooks


async def sendText(text: str):
    print("Text")
    async with aiohttp.ClientSession() as session:
        webhook_urls = hooks.all_hooks()
        print(webhook_urls)
        for url in webhook_urls[0]:
            wh = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            e = Embed(title="📑 Новости", description=text, color=Colour.blue())
            await wh.send(embed=e)


async def sendPhoto(text: str, photo_path: str):
    async with aiohttp.ClientSession() as session:
        for url in hooks.all_hooks()[0]:
            wh = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            e = Embed(title="📑 Новости", description=text, color=Colour.blue())
            await wh.send(embed=e, file=File(photo_path))
            os.remove(photo_path)


async def sendVideo(text: str, video_path: str):
    async with aiohttp.ClientSession() as session:
        for url in hooks.all_hooks()[0]:
            wh = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            e = Embed(title="📑 Новости", description=text, color=Colour.blue())
            await wh.send(embed=e, file=File(video_path))
            os.remove(video_path)


if __name__ == "__main__":
    print("Do not run this file. Use \033[94mdocker build .\033[0m at root of project")
