from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("24509126"))
API_HASH = getenv("2c1e3e02b9e1b0a3f9c7955d5d55a1d5")

BOT_TOKEN = getenv("7370991491:AAH6MOfqJKTI8vo7uNELIZ4wKuAv91WPak4")
MONGO_DB_URI = getenv("mongodb+srv://codaga9286:JgH1nbOW5JSXUO4U@cluster0.if4xdya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

OWNER_ID = int(getenv("OWNER_ID", 6127347210))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/taporibot_bot")
