import redis
from telegram import Update
from telegram.ext import ContextTypes

# Connect to Redis (assumes Redis is running locally)
r = redis.Redis(host='localhost', port=6379, db=0)

def is_rate_limited(user_id):
    key = f"rate_limit:{user_id}"
    count = r.get(key)
    if not count:
        r.set(key, 1, ex=3600)  # Set key with 1-hour TTL
        return False
    elif int(count) < 100:  # Allow 100 requests per hour
        r.incr(key)
        return False
    return True

def rate_limit_decorator(func):
    def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if is_rate_limited(user_id):
            update.message.reply_text("Rate limit exceeded. Try again later.")
            return
        return func(update, context)
    return wrapper