import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

# Initialize the bot
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

# Set up logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Import command handlers from the commands module
from commands.start import start
from commands.ip import ip_osint
from commands.whois import whois_domain
from commands.social import social_lookup
from commands.email import email_osint
from commands.phone import phone_osint
from commands.image import image_osint
from commands.help import help_command

# Add command handlers to the dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('ip', ip_osint))
dp.add_handler(CommandHandler('whois', whois_domain))
dp.add_handler(CommandHandler('social', social_lookup))
dp.add_handler(CommandHandler('email', email_osint))
dp.add_handler(CommandHandler('phone', phone_osint))
dp.add_handler(MessageHandler(Filters.photo, image_osint))
dp.add_handler(CommandHandler('help', help_command))

# Handler for unknown commands
def unknown(update, context):
    update.message.reply_text("Sorry, I didn't understand that command.")
dp.add_handler(MessageHandler(Filters.command, unknown))

# Start the bot
updater.start_polling()
updater.idle()