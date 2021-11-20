from environs import Env
from pathlib import Path

# Вместо библиотеки python-dotenv изпользуем environs
env = Env()
env.read_env()

# === TGM ===
TG_TOKEN = env.str("TG_TOKEN")

# === DS ===
DS_TOKEN = env.str("DS_TOKEN")
DS_INVITE_LINK = f"https://discordapp.com/oauth2/authorize?client_id={env.int('DS_APP_ID')}&scope=bot&permissions={env.int('DS_ACCESS')}"

# === SYSTEM ===
DIR = str(Path(__file__).parent.parent)
