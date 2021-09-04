import os
from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import filters, Client

# logging......

bot = Client(
   "Music-Bot",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN,
)
bot.run()


