import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Raganork user"
PM_IMG = "https://telegra.ph/file/0e00f9e103c4a21ed35a5.jpg"
pm_caption = "🔥🔥**Ɽǟɢǟռօʀӄɮð† IS ON FIRE🔥🔥\n\n"

on_caption += f"⚔️⚔️**му ℓσя∂**⚔️⚔️   : {DEFAULTUSER}\n"

on_caption += "⚡️⚡️**тєℓєтнσи**⚡️⚡️   : 1.15.0 \n"

on_caption += "⚡️⚡️**Os[Linux]**⚡️⚡️   : ʟɪɴᴜx ᴍᴀɴᴅʀɪᴠᴀ \n"

on_caption += "😈😈**Ɽǟɢǟռօʀӄɮð†**😈😈   : 2.0\n"

on_caption += "✨✨**¢нαииєℓ**✨✨   : [ᴊᴏɪɴ](https://t.me/Raganork_Official)\n"

on_caption += "⚜️⚜️**gяσυρ**⚜️⚜️   : [ᴊᴏɪɴ](https://t.me/Raganork_bot_chat)\n"

on_caption += "💫💫**ᴄᴜʀʀᴇɴᴛ ᴅɪʀᴇᴄᴛᴏʀʏ**💫💫   : ᴋᴀʟɪ_ᴘᴀʀʀᴏᴛ_ᴛᴇʀᴍɪɴᴀʟ\n"

on_caption += "__I am here alive with my sweet master till my dyno runs off!!!😎__ \n"

on_caption += "🔥🔥**ᴅᴇᴠᴇʟᴏᴘᴇʀ**🔥🔥   :   [Raganork-Owner](https://t.me/HELLBOY_OP)\n"


on_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/HELLBOY_OP)\n"
@borg.on(admin_cmd(pattern=r"on"))
async def amireallyalive(lol):
    chat = await lol.get_chat()
    await lol.delete()
    """ For .on command, check if I am on(alive) fire or not.  """
    await borg.send_file(lol.chat_id, PM_IMG,caption=on_caption)
    await alive.delete()
