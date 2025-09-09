from telegram.ext import Updater, MessageHandler, Filters
import yt_dlp

TOKEN = "8469651505:AAG0q5m1PODoPnBfOFm984xWLzI8Y7gxqCA"

def download_audio(update, context):
    url = update.message.text
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audio.mp3",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    update.message.reply_audio(open("audio.mp3", "rb"))

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_audio))

updater.start_polling()
updater.idle()
