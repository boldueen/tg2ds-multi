from environs import Env
from pathlib import Path

# Вместо библиотеки python-dotenv изпользуем environs
env = Env()
env.read_env()

# === TGM ===
ADMINS = env.list("ADMINS")
TG_TOKEN = env.str("TG_TOKEN")

# === DS ===
DS_TOKEN = env.str("DS_TOKEN")

# === SYSTEM ===
DIR = str(Path(__file__).parent.parent)
