import whois
from telegram import Update
from telegram.ext import ContextTypes
from utils.rate_limit import rate_limit_decorator

@rate_limit_decorator
def whois_domain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        update.message.reply_text("Usage: /whois <domain>")
        return
    domain = context.args[0]
    try:
        w = whois.whois(domain)
        result = (
            f"*WHOIS Results for {domain}*\n"
            f"- Registrar: {w.registrar or 'N/A'}\n"
            f"- Creation Date: {w.creation_date or 'N/A'}\n"
            f"- Expiration Date: {w.expiration_date or 'N/A'}\n"
            f"- Name Servers: {', '.join(w.name_servers) if w.name_servers else 'N/A'}"
        )
        update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")