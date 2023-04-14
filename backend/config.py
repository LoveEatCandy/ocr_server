import os

APP_KEY = os.environ.get("APP_KEY")
APP_SECRET = os.environ.get("APP_SECRET")

STATIC_DIR = "static"
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR, exist_ok=True)
DB_DIR = "db"
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR, exist_ok=True)
IMG_RECORD_FILE = os.path.join(DB_DIR, "imgs.txt")
if not os.path.exists(IMG_RECORD_FILE):
    with open(IMG_RECORD_FILE, "wb") as f:
        pass
IMG_RESULT_FILE = os.path.join(DB_DIR, "result.jsonl")
if not os.path.exists(IMG_RESULT_FILE):
    with open(IMG_RESULT_FILE, "wb") as f:
        pass
