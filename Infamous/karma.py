# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/f716e222e29e5cd701b3d.jpg",
    "https://telegra.ph/file/8351a53ee3c648c843ee2.jpg",
    "https://telegra.ph/file/30f31fa0a4fdd6951526a.jpg",

"https://telegra.ph/file/927b0d254b6cd77dc249c.jpg",

"https://telegra.ph/file/8a4df596c5c29d2c4580f.jpg",
]

HEY_IMG = "https://telegra.ph/file/f716e222e29e5cd701b3d.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/927b0d254b6cd77dc249c.jpg",
]

BAN_GIFS = [
    "https://telegra.ph/file/83aeb5ab51e7e742af9cd.jpg",
]


KICK_GIFS = [
    "https://telegra.ph/file/43fca023276c21ada04ba.jpg",
]


MUTE_GIFS = [
    "https://telegra.ph/file/cc507a89bb998928643fc.jpg",
]

FIRST_PART_TEXT = "✨ *ᴇʏᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ᴋᴇɴᴀʟɪɴ ɴᴀᴍᴀ sᴀʏᴀ ᴋᴏʙᴏ ᴋᴀɴᴀᴇʀᴜ, sᴀʏᴀ ᴀᴅᴀʟᴀʜ ʀᴏʙᴏᴛ ᴍᴇɴᴇᴊᴇᴍᴇɴ ʙᴇʀᴛᴇᴍᴀ ᴀɴɪᴍᴇ ᴅᴀʀɪ ᴠᴛᴜʙᴇʀ, ᴀᴅᴀ ʏᴀɴɢ ʙɪsᴀ ᴋᴏʙᴏ ʙᴀɴᴛᴜ?*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴋᴏʙᴏ ᴋᴇ ɢʀᴜᴘ ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="📚 ғɪᴛᴜʀ 📚", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="🔎 ᴅᴇᴛᴀɪʟ 🔍", callback_data="Miko_"),
        InlineKeyboardButton(text="🤖 ᴀɪ ʙᴏᴛ 🤖", callback_data="ai_handler"),
        InlineKeyboardButton(text="🏡 ɢʀᴏᴜᴘ 🏡", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(text="👑 ᴏᴡɴᴇʀ 👑", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴋᴏʙᴏ ᴋᴇ ɢʀᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/skyskykyy"),
        ib(text="SUPPORT", url="https://t.me/wibuhouse"),
    ],
    [
        ib(
            text="ᴀᴅᴅ ᴋᴏʙᴏ ᴋᴀɴᴀᴇʀᴜ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *𝐊𝐨𝐛𝐨 𝐊𝐚𝐧𝐚𝐞𝐫𝐮 𝐁𝐨𝐭* 🫧

☉ *Di sini, Anda akan menemukan daftar semua perintah yang tersedia*.

sᴇᴍᴜᴀ ғɪᴛᴜʀ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅᴇɴɢᴀɴ ᴘᴇʀɪɴᴛᴀʜ
ᴄᴏɴᴛᴏʜ : /start
"""
