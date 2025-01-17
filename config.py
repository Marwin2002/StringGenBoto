from os import getenv
import os
from dotenv import load_dotenv

load_dotenv()


API_ID = os.getenv("API_ID", "12380656")
API_HASH = os.getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://architect2002:architect2002@cluster0.ccinu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 7224419362))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/The_Architect04")
MUST_JOIN = getenv("MUST_JOIN", "The_Architect04")
