import telebot



bot = telebot.TeleBot("6782521207:AAEItXW8Ukf18hJ8BLvCwwvqrq2DpqD0mdA")
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


