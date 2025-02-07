from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    telegram_api_key = os.getenv("TELEGRAM_API_KEY")
    database_url = os.getenv("DATABASE_URL")


def get_settings():
    return Config()