# GitHub: github.com/boldueen github.com/mdpanf
# Telegram: t.me/realnikonoff t.me/mdpanf
# WEB-pages: uadd.me/mdpanf

from aiogram import executor
from utils.loader import dp
from utils import logger
from utils import telechan

logo = f"""\033[92m
  ____ _ _ _       \033[33mby\033[92m          ____            _           _
 / ___(_) | |_   _ _ __ ___   |  _ \ _ __ ___ (_) ___  ___| |_
| |   | | | | | | | '_ ` _ \  | |_) | '__/ _ \| |/ _ \/ __| __|
| |___| | | | |_| | | | | | | |  __/| | | (_) | |  __/ (__| |_
 \____|_|_|_|\__,_|_| |_| |_| |_|   |_|  \___// |\___|\___|\__|
                           \033[94mt.me/realnikonoff\033[92m |__/  \033[94mt.me/mdpanf\033[0m
"""


if __name__ == '__main__':
    print(logo)
    executor.start_polling(dp)
