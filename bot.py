#!venv/bin/python3

from dotenv import load_dotenv
import os, telebot
import __app__ as __app__
import __state_user__
from handlers import register_handlers

load_dotenv('.env') # Memuat variabel lingkungan dari file .env
BOT_TOKEN = os.environ.get('BOT_TOKEN') 
bot = telebot.TeleBot(str(BOT_TOKEN))

# Mendaftarkan semua handler dari modul handlers
register_handlers(bot)

if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print("\n[+] Bot dihentikan.")
    except Exception as e:
        print(f"[+] Terjadi error: {e}")