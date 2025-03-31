from telethon.sync import TelegramClient
from pyrogram import Client

async def generate_telethon_session(app, phone_number, otp):
    telethon_client = TelegramClient(phone_number, app.api_id, app.api_hash)
    await telethon_client.connect()
    await telethon_client.send_code_request(phone_number)
    await telethon_client.sign_in(phone_number, otp)
    return telethon_client

async def generate_pyrogram_session(app, phone_number, otp):
    await app.send_code(phone_number)
    session = await app.sign_in(phone_number, app.phone_code_hash, otp)
    return session.string
