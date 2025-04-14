import telebot

TOKEN = "7678852248:AAEBC-ZEpLv5t57MRaFh0L11fW1RiwXTyd4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Assalomu alaykum! SHAXAMVP UC BOT ga xush kelibsiz!")

bot.infinity_polling()
# okee restart
