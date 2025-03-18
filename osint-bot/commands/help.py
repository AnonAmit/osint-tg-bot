from telegram import Update
from telegram.ext import ContextTypes

def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = (
        "Available commands:\n"
        "/phone <number> - Perform OSINT on a phone number.\n"
        "/email <email> - Check for breaches and linked accounts.\n"
        "/ip <IP> - Perform IP lookup, WHOIS, and geolocation tracking.\n"
        "/whois <domain> - Get domain information and subdomains.\n"
        "/social <username> - Search username across multiple social platforms.\n"
        "/image <upload> - Reverse image search and metadata extraction."
    )
    update.message.reply_text(help_message)