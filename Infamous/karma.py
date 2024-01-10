# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/aa797e9e3b268b8c095da.jpg",
    "https://telegra.ph/file/332d9f8cdc7ad1564c87a.jpg",
    "https://telegra.ph/file/14ef2c1b556a60bb696c6.jpg",
]

HEY_IMG = "https://telegra.ph/file/aa797e9e3b268b8c095da.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/10bfafd05cb8a4927edff.jpg",
]

BAN_GIFS = [
    "https://telegra.ph/file/9288325c28518d8cf4ada.jpg",
]


KICK_GIFS = [
    "https://telegra.ph/file/16ac083559851a92a5113.jpg",
]


MUTE_GIFS = [
    "https://telegra.ph/file/9331a9fc5b04594a36d09.jpg",
]

FIRST_PART_TEXT = "✨ *ʜᴀʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɴᴀᴍᴀ ᴋᴜ ᴘᴀɪᴍᴏɴ ᴀᴋᴜ ᴀᴅᴀʟᴀʜ ʀᴏʙᴏᴛ ᴍᴇɴᴇᴊᴇᴍᴇɴ ʙᴇʀᴛᴇᴍᴀ ᴋᴀɴ ᴀᴍɪɴᴇ ᴅᴀʀɪ ɢᴇɴsʜɪɴ ɪᴍᴘᴀᴄᴛ, ʏᴜ ᴀᴅᴅ ᴘᴀɪᴍᴏɴ ʀᴏʙᴏᴛ ᴋᴇ ᴅᴀʟᴀᴍ ɢʀᴜᴘ ᴍᴜ sᴇᴋᴀʀᴀɴɢ ᴛʜɴᴋs*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴘᴀɪᴍᴏɴ ➕",
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
            text="ᴀᴅᴅ ᴘᴀɪᴍᴏɴ ᴋᴇ ɢʀᴜᴘ",
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
        ib(text="UPDATES", url="https://t.me/Hydra_Updates"),
        ib(text="SUPPORT", url="https://t.me/hydraXsupport"),
    ],
    [
        ib(
            text="ᴀᴅᴅ ᴘᴀɪᴍᴏɴ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *𝐏ᴀɪᴍᴏɴ 𝐁ᴏᴛ* 🫧

☉ *Di sini, Anda akan menemukan daftar semua perintah yang tersedia*.

sᴇᴍᴜᴀ ғɪᴛᴜʀ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅᴇɴɢᴀɴ ᴘᴇʀɪɴᴛᴀʜ
ᴄᴏɴᴛᴏʜ : /start
"""
