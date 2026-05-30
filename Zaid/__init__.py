import os
from pyrogram import Client

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
STRING_SESSION1 = os.environ.get("STRING_SESSION1")

# ✅ TAMBAH INI — clients dan ids
clients = []
ids = []

# ✅ app dengan session_string
app = Client(
    "my_client",
    api_id=int(API_ID),
    api_hash=API_HASH,
    session_string=STRING_SESSION1,
    app_version="4.20.0",
    device_model="Linux"
)
