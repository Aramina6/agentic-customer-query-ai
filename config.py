import os
from dotenv import load_dotenv

load_dotenv()  # reads .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Set OPENAI_API_KEY in .env")
