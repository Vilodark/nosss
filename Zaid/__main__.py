import asyncio
import importlib
import os  # ✅ TAMBAH INI
from pyrogram import Client, idle
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, ids  # ✅ HAPUS "app" dari sini

# ✅ TAMBAH INI
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
STRING_SESSION1 = os.environ.get("STRING_SESSION1")

# ✅ GANTI app ini — definisikan ulang
app = Client(
    "my_client",
    api_id=int(API_ID),
    api_hash=API_HASH,
    session_string=STRING_SESSION1  # ✅ Pakai session string
)

async def start_bot():
    await app.start()
    print("LOG: Userbot started with STRING_SESSION 🔥")  # ✅ GANTI INI
    for all_module in ALL_MODULES:
        importlib.import_module("Zaid.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
