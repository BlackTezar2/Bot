import telebot
import requests
from datetime import datetime
import feedparser

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

def get_btc():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    return requests.get(url).json()['bitcoin']['usd']

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "به ربات CryptYumy خوش اومدی! 🍬\n\nدستورات:\n/btc - قیمت بیت‌کوین\n/eth - قیمت اتریوم")

@bot.message_handler(commands=['btc'])
def btc(message):
    price = get_btc()
    bot.reply_to(message, f"💰 بیت‌کوین: ${price:,.0f}")

bot.infinity_polling()
