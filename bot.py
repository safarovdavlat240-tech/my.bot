import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
TOKEN = os.environ.get("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Салом! Бот кор мекунад! 🚀")
app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot is alive!"
def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)
def main():
    threading.Thread(target=run_flask).start()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
if __name__ == '__main__':
    main()
