from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.loader import dp
from aiogram.dispatcher.filters.builtin import Command

from utils.dischan import sendText, sendPhoto, sendVideo

from utils import logger
from data.config import DS_INVITE_LINK


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


@dp.message_handler(Command(["link", "start", "help"]))
async def get_link(msg: types.Message):
    text = f"Ссылка для приглашения бота:\n<code>{DS_INVITE_LINK}</code>"
    reply_markup = InlineKeyboardMarkup().add(InlineKeyboardButton("🤖 Пригласить", url=DS_INVITE_LINK))
    await msg.answer(text=text, reply_markup=reply_markup, parse_mode=types.ParseMode.HTML)


if __name__ == "__main__":
    print("Do not run this file. Use \033[94mdocker build .\033[0m at root of project")
