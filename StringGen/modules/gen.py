from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from StringGen import Anony
from StringGen.helpers import generate_telethon_session, generate_pyrogram_session

async def gen_session(client: Client, message, type):
    user_id = message.from_user.id
    await message.edit("Processing...")
    app = client
    if type == "telethon":
        await message.edit(
            "Generating Telethon session...\nPlease enter your phone number (e.g., +1234567890)"
        )
        phone = await app.listen(user_id, timeout=60)  # Timeout set to 60 seconds directly
        if not phone:
            return await message.edit("Session generation cancelled due to timeout.")
        await app.delete_messages(user_id, phone.id)
        phone_number = phone.text
        await message.edit(f"Phone Number: {phone_number}\n\nNow enter the OTP sent to this number.")
        code = await app.listen(user_id, timeout=60)  # Timeout set to 60 seconds directly
        if not code:
            return await message.edit("Session generation cancelled due to timeout.")
        await app.delete_messages(user_id, code.id)
        otp = code.text
        try:
            telethon_client = await generate_telethon_session(app, phone_number, otp)
            session_str = telethon_client.session.save()
            await message.edit(f"Telethon Session Generated Successfully!\n\n{session_str}\n\nNote: Save this string securely. Do not share it publicly!")
        except Exception as e:
            await message.edit(f"Error: {str(e)}")
    elif type == "pyrogram":
        await message.edit(
            "Generating Pyrogram session...\nPlease enter your phone number (e.g., +1234567890)"
        )
        phone = await app.listen(user_id, timeout=60)  # Timeout set to 60 seconds directly
        if not phone:
            return await message.edit("Session generation cancelled due to timeout.")
        await app.delete_messages(user_id, phone.id)
        phone_number = phone.text
        await message.edit(f"Phone Number: {phone_number}\n\nNow enter the OTP sent to this number.")
        code = await app.listen(user_id, timeout=60)  # Timeout set to 60 seconds directly
        if not code:
            return await message.edit("Session generation cancelled due to timeout.")
        await app.delete_messages(user_id, code.id)
        otp = code.text
        try:
            session_str = await generate_pyrogram_session(app, phone_number, otp)
            await message.edit(f"Pyrogram Session Generated Successfully!\n\n{session_str}\n\nNote: Save this string securely. Do not share it publicly!")
        except Exception as e:
            await message.edit(f"Error: {str(e)}")
