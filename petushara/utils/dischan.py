import os

import aiohttp
from discord import Embed, Webhook, AsyncWebhookAdapter, Colour, File

from utils.loader import hooks

from utils import logger


async def sendText(text: str):
    try:
        async with aiohttp.ClientSession() as session:
            urls = hooks.all_hooks()
            for url in urls:
                wh = Webhook.from_url(url[0], adapter=AsyncWebhookAdapter(session))
                e = Embed(title="📑 Новости", description=text, color=Colour.blue())
                await wh.send(embed=e)
    except Exception as e:
        logger.logging.error(e)


async def sendPhoto(text: str, photo_path: str):
    try:
        async with aiohttp.ClientSession() as session:
            urls = hooks.all_hooks()
            for url in urls:
                wh = Webhook.from_url(url[0], adapter=AsyncWebhookAdapter(session))
                e = Embed(title="📑 Новости", description=text, color=Colour.blue())
                e.set_image(url=f"attachment://{photo_path}")
                await wh.send(embed=e, file=File(photo_path))
            os.remove(photo_path)
    except Exception as e:
        os.remove(photo_path)
        logger.logging.error(e)


async def sendVideo(text: str, video_path: str, msg_id):
    try:
        async with aiohttp.ClientSession() as session:
            urls = hooks.all_hooks()
            for url in urls:
                wh = Webhook.from_url(url[0], adapter=AsyncWebhookAdapter(session))
                e = Embed(title="📑 Новости", description=text, color=Colour.blue())
                await wh.send(embed=e, file=File(video_path))
            os.remove(video_path)
    except Exception as e:
        os.remove(video_path)
        logger.logging.error(e)
        try:
            async with aiohttp.ClientSession() as session:
                urls = hooks.all_hooks()
                text = f"{text}\n\n_🎬 Видео смотреть в [telegram](https://t.me/projectarmor/{msg_id})_"
                for url in urls:
                    wh = Webhook.from_url(url[0], adapter=AsyncWebhookAdapter(session))
                    e = Embed(title="📑 Новости", description=text, color=Colour.blue())
                    await wh.send(embed=e)
                os.remove(video_path)
        except Exception as e:
            logger.logging.error(e)


if __name__ == "__main__":
    print("Do not run this file. Use \033[94mdocker build .\033[0m at root of project")
