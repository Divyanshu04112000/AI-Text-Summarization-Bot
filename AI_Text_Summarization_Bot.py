import os
from dotenv import load_dotenv
import telebot
import cohere

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not COHERE_API_KEY or not TELEGRAM_BOT_TOKEN:
    raise ValueError("Please set COHERE_API_KEY and TELEGRAM_BOT_TOKEN in the .env file.")

# Create a Cohere client instance
co = cohere.Client(COHERE_API_KEY)

# Create a Telegram bot instance
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Define a handler for incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text

    try:
        # Use Cohere to summarize the text
        response = co.summarize(
            text=text,
            length='auto',
            format='auto',
            model='summarize-xlarge',
            additional_command='',
            temperature=0.3,
        )
        summary = response.summary
        bot.reply_to(message, summary)

    except Exception as e:
        print("Error:", str(e))
        bot.reply_to(message, "Oops! Something went wrong.")

# Start the Telegram bot
bot.polling()
