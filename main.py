import telebot



bot = telebot.TeleBot("6336490086:AAEpQooiX8qpOQ-DY7ohRGSqcJ05KwwG2f4")
bot.remove_webhook()

@bot.message_handler()
def Myfunc(message):
  bot.send_message(message.chat.id, "Hi, What's happend?")





from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
  return "<b> hello</b>"

def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()

bot.infinity_polling(skip_pending=True)


