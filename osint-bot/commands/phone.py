import phonenumbers
from telegram import Update
from telegram.ext import ContextTypes
from utils.rate_limit import rate_limit_decorator

@rate_limit_decorator
def phone_osint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        update.message.reply_text("Usage: /phone <number>")
        return
    number = context.args[0]
    try:
        parsed = phonenumbers.parse(number, None)
        if phonenumbers.is_valid_number(parsed):
            result = (
                f"*Phone Number Validation*\n"
                f"- Valid: Yes\n"
                f"- Country: {phonenumbers.region_code_for_number(parsed)}"
            )
        else:
            result = "*Phone Number Validation*\n- Valid: No"
        update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")