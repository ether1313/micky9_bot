import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8584825318:AAHFlB4rh9_w0td01YWXYQNeiSpkVB8t92s")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/micky13_au")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://micky9.net/RFMICKYBOT")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://micky9.net/RFMICKYBOT")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Micky9 Promo Bot"
BOT_DESCRIPTION = "Micky9 Marketing Assistant - Provides latest promotions and event information"
