from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
import yt_dlp
import os

TOKEN = "8874137889:AAE33bAAK6QLceoD6xx9CMBFQva7bp52KhA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Linki YouTube ravon kun!")

async def get_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "youtube.com" not in url and "youtu.be" not in url and "tiktok.com" not in url:
        await update.message.reply_text("Faqat YouTube/TikTok!")
        return
    await update.message.reply_text("Downloading...")
    try:
        opts = {'format': 'bestaudio/best', 'outtmpl': '%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file = ydl.prepare_filename(info)
        with open(file, 'rb') as f:
            await update.message.reply_audio(audio=f, title=info.get('title'))
        os.remove(file)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_music))
print("Bot started!")
app.run_polling()