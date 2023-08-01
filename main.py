import os

from flask import Flask, request

import telebot

TOKEN = '6336490086:AAEpQooiX8qpOQ-DY7ohRGSqcJ05KwwG2f4'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

@app.route("/")
def hello():
    return request.base_url

@app.route('/ahmed', methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200




@app.route("/set")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=request.base_url + "ahmed")
    return "!", 200


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)