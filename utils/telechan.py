from aiogram import types
from utils.loader import dp

from utils.dischan import sendText, sendPhoto, sendVideo

from utils import logger


async def parse(msg):
    # Parse text
    text = msg.parse_entities(as_html=False)
    text = text.replace('*', '**')
    text = text.replace('\\\#', '#')
    return text


@dp.channel_post_handler(content_types=types.ContentTypes.TEXT)
async def text_in_channel(msg: types.Message):
    try:
        text = await parse(msg)
        await sendText(text)
    except Exception as e:
        logger.logging.error(e)


@dp.channel_post_handler(content_types=types.ContentTypes.PHOTO)
async def photo_in_channel(msg: types.Message):
    try:
        text = ''
        photo_path = f"{msg.chat.title}_{msg.message_id}.png"
        await msg.photo[-1].download(destination_file=photo_path)
        if 'caption' in msg:
            text = await parse(msg)
        await sendPhoto(text, photo_path)
    except Exception as e:
        logger.logging.error(e)


@dp.channel_post_handler(content_types=types.ContentTypes.VIDEO)
async def video_in_channel(msg: types.Message):
    try:
        text = ''
        video_path = f"{msg.chat.title}_{msg.message_id}.mp4"
        await msg.video.download(destination_file=video_path)
        if 'caption' in msg:
            text = await parse(msg)
        await sendVideo(text, video_path, msg.message_id)
    except Exception as e:
        logger.logging.error(e)


if __name__ == "__main__":
    print("Do not run this file. Use \033[94mdocker build .\033[0m at root of project")
