import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Салом! Бот кор мекунад! 🚀")

if __name__ == '__main__':
    token = os.getenv("BOT_TOKEN")
    print(f"Token bor: {bool(token)}")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is alive!")
    app.run_polling()
