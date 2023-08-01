import telebot
from flask import Flask, request

# Set up Flask app
app = Flask(__name__)

# Define your Telegram bot tokens
token = '6336490086:AAEpQooiX8qpOQ-DY7ohRGSqcJ05KwwG2f4'

# Create instances of Telebot for each bot
bot1 = telebot.TeleBot(token)




@app.route('/', methods=['GET'])
def bot1_webhook():
    return 'OK'

# Define a route for receiving webhook updates from Telegram
@app.route('/bot_webhook', methods=['POST'])
def bot_webhook():
    bot1.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])

    return 'OK'





# Handle '/start' command for both bots
@bot1.message_handler(commands=['start'])
def bot1_start(message):
    bot1.send_message(message.chat.id, "Hello! I am Bot 1. Let's do some addition.")



bot1.remove_webhook()
bot1.set_webhook("https://my-flask-heroku-535f0de7db25.herokuapp.com/bot_webhook")


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
