from telegram import Update
from telegram.ext import ContextTypes
import pyexiftool
import os

def image_osint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]  # Get the highest resolution photo
    file = context.bot.get_file(photo.file_id)
    file.download('temp_image.jpg')
    try:
        with pyexiftool.ExifTool() as et:
            metadata = et.get_metadata('temp_image.jpg')
        result = "*Image Metadata*\n"
        for key, value in metadata.items():
            result += f"- {key}: {value}\n"
        result += "\n*Reverse Image Search:*\n"
        result += "- [Google Lens](https://lens.google.com/upload)\n"
        result += "- [Yandex Images](https://yandex.com/images/)\n"
        result += "- [PimEyes](https://pimeyes.com/en)"
        update.message.reply_text(result, parse_mode='Markdown', disable_web_page_preview=True)
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")
    finally:
        if os.path.exists('temp_image.jpg'):
            os.remove('temp_image.jpg')