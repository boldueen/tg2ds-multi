import aiohttp
from discord import Embed, Webhook, AsyncWebhookAdapter, Colour, File


webhook_urls = (
    "1234",
    "5678"
)


async def sendText(text: str):
    async with aiohttp.ClientSession() as session:
        for url in webhook_urls:
            wh = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            e = Embed(title="📑 Новости", description=text, color=Colour.blue())
            await wh.send(embed=e)


async def sendPhoto(text: str, photo_path: str):
    async with aiohttp.ClientSession() as session:
        for url in webhook_urls:
            wh = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            e = Embed(title="📑 Новости", description=text, color=Colour.blue())
            await wh.send(embed=e, file=File(photo_path))


async def sendVideo(text: str, video_path: str):
    async with aiohttp.ClientSession() as session:
        for url in webhook_urls:
            wh = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            e = Embed(title="📑 Новости", description=text, color=Colour.blue())
            await wh.send(embed=e, file=File(video_path))


if __name__ == "__main__":
    print("Do not run this file. Use \033[94mdocker build .\033[0m at root of project")
