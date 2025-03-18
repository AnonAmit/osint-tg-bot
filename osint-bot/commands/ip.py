import requests
from telegram import Update
from telegram.ext import ContextTypes
from ipaddress import ip_address
from utils.rate_limit import rate_limit_decorator

@rate_limit_decorator
def ip_osint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        update.message.reply_text("Usage: /ip <IP>")
        return
    ip = context.args[0]
    try:
        ip_address(ip)  # Validate IP address
        msg = update.message.reply_text(f"Processing IP lookup for {ip}...")
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url).json()
        result = (
            f"*IP Lookup Results*\n"
            f"- IP: {ip}\n"
            f"- Location: {response.get('city', 'N/A')}, {response.get('country', 'N/A')}\n"
            f"- Organization: {response.get('org', 'N/A')}"
        )
        context.bot.edit_message_text(
            chat_id=msg.chat_id,
            message_id=msg.message_id,
            text=result,
            parse_mode='Markdown'
        )
    except ValueError:
        update.message.reply_text("Invalid IP address.")
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")
