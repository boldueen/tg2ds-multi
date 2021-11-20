# GitHub: github.com/boldueen github.com/mdpanf
# Telegram: t.me/realnikonoff t.me/mdpanf
# WEB-pages: uadd.me/mdpanf

from aiogram import executor, types

from utils import logger, telechan
from utils.loader import dp

logo = f"""\033[92m
  ____ _ _ _       \033[33mby\033[92m          ____            _           _
 / ___(_) | |_   _ _ __ ___   |  _ \ _ __ ___ (_) ___  ___| |_
| |   | | | | | | | '_ ` _ \  | |_) | '__/ _ \| |/ _ \/ __| __|
| |___| | | | |_| | | | | | | |  __/| | | (_) | |  __/ (__| |_
 \____|_|_|_|\__,_|_| |_| |_| |_|   |_|  \___// |\___|\___|\__|
                           \033[94mt.me/realnikonoff\033[92m |__/  \033[94mt.me/mdpanf\033[0m
"""

if __name__ == '__main__':
    logger.logging.debug(logger.__name__ + " imported successfully")
    logger.logging.info(logo)
    logger.logging.debug(telechan.__name__ + " imported successfully")
    executor.start_polling(dp)
