import telebot

token = '1877422283:AAG0oeNDiP_QVgHvcbKk_NUpr2ZiDzH_Yuk'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
