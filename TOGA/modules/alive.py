import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from TOGA.events import register
from TOGA import telethn as tbot


PHOTO = "https://te.legra.ph/file/82265204b556d514a3a1b.jpg"

@register(pattern=("/alive"))
async def awake(event):
  text2 = f"**Heyaa.. Weeb! [{event.sender.first_name}](tg://user?id={event.sender.id}), I'M Akira.** \n\n"
  text2 += "⁜ **I'll Be Giving My Best For Your Work !!** \n\n"
  text2 += f"⁜ **Library Version :** `{telever}` \n\n"
  text2 += f"⁜ **Telethon Version :** `{tlhver}` \n\n"
  text2 += f"⁜ **Pyrogram Version :** `{pyrover}` \n\n"
  text2 += "**⁜Thanks For Adding Me Here ⁜**"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/AstorPro"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/AstorSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=text2,  buttons=BUTTON)
