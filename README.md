# AI-Text-Summarization-Bot
A simple Telegram bot that uses Cohere’s Summarization API to create concise summaries of text sent by users.

✨ Features
Accepts any text message from Telegram.

Uses Cohere AI to summarize content.

Sends the summarized result back instantly.

Easy to set up and run locally or on a server.

📦 Requirements
Python 3.8+

Telegram bot token (from BotFather)

Cohere API key (from Cohere)

Libraries:

cohere

telebot

requests

🔧 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/AI_Text_Summarization_Bot.git
cd AI_Text_Summarization_Bot
Install dependencies

bash
Copy
Edit
pip install cohere telebot requests
Set environment variables
Create a .env file and add:

env
Copy
Edit
COHERE_API_KEY=your_cohere_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
🚀 Usage
Run the bot:

bash
Copy
Edit
python AI_Text_Summarization_Bot.py
Now send a message to your Telegram bot, and it will reply with a summarized version.

📌 Notes
Do not hardcode API keys in your code when pushing to GitHub.

Use .env files or environment variables for security.

The summarization quality depends on the input text and Cohere’s model.

📄 License
This project is licensed under the MIT License.
