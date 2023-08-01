from flask import Flask
from threading import Thread
from flask import request
app = Flask(__name__)


link = ""
@app.route('/')
def home():
  global link
  link = request.base_url

  return request.base_url

def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()



import telebot

bot = telebot.TeleBot("6336490086:AAEpQooiX8qpOQ-DY7ohRGSqcJ05KwwG2f4")

@bot.message_handler()
def Myfunc(message):
    bot.send_message(message.chat.id, "Hi, What's happend?")

@app.route('/bot_webhook', methods=['POST'])
def bot_webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])

    return 'OK'


bot.remove_webhook()

bot.set_webhook(f"{link}bot_webhook")

keep_alive()