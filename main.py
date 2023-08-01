from flask import Flask, request
import telebot

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot_token = '6336490086:AAEpQooiX8qpOQ-DY7ohRGSqcJ05KwwG2f4'
bot = telebot.TeleBot(bot_token)

@app.route('/')
def index():
    return "Hello, this is your Telegram bot!"

# This is the endpoint where Telegram will send updates
@app.route('/telegram-webhook', methods=['POST'])
def webhook():
    # Get the data from Telegram's POST request
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return ''


webhook_url = 'https://my-flask-heroku-535f0de7db25.herokuapp.com' + '/telegram-webhook'

# Set the webhook
bot.remove_webhook()
bot.set_webhook(url=webhook_url)




if __name__ == '__main__':
    # Start Flask app
    app.run(debug=True)
