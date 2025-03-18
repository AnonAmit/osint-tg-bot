import requests
from telegram import Update
from telegram.ext import ContextTypes
from utils.rate_limit import rate_limit_decorator

@rate_limit_decorator
def social_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        update.message.reply_text("Usage: /social <username>")
        return
    username = context.args[0]
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Facebook": f"https://facebook.com/{username}",
        "LinkedIn": f"https://linkedin.com/in/{username}"
    }
    results = []
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                results.append(f"{platform}: Found")
            else:
                results.append(f"{platform}: Not Found")
        except Exception:
            results.append(f"{platform}: Error")
    result_text = "\n".join(results)
    update.message.reply_text(f"*Social Media Lookup for {username}*\n{result_text}", parse_mode='Markdown')