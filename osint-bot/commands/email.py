import requests
from telegram import Update
from telegram.ext import ContextTypes
from utils.rate_limit import rate_limit_decorator

@rate_limit_decorator
def email_osint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        update.message.reply_text("Usage: /email <email>")
        return
    email = context.args[0]
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {'User-Agent': 'OSINT-Bot'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            breach_list = [breach['Name'] for breach in breaches]
            result = f"*Breaches found for {email}*\n" + "\n".join(breach_list)
        elif response.status_code == 404:
            result = f"No breaches found for {email}"
        else:
            result = "Error checking breaches"
        update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")