from os import getenv


API_ID = int(getenv("API_ID", "21191737"))
API_HASH = getenv("API_HASH", "d7147a78a97a1dc3839f9bd3b24fb8bc")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_URL = getenv("MONGO_URL", "")
SESSION_STRING = getenv("SESSION_STRING", "")


