import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Raganork User"
PM_IMG = "https://telegra.ph/file/0e00f9e103c4a21ed35a5.jpg"
pm_caption = "🔥🔥**Ɽǟɢǟռօʀӄɮð† IS ONLINE🔥🔥\n\n"

pm_caption += f"⚔️⚔️**му ℓσя∂**⚔️⚔️: {DEFAULTUSER}\n\n"

pm_caption += "⚡️⚡️**тєℓєтнσи**⚡️⚡️: 1.15.0 \n\n"

pm_caption += "⚡️⚡️**Os[Linux]**⚡️⚡️: ʟɪɴᴜx ᴍᴀɴᴅʀɪᴠᴀ \n\n"

pm_caption += "😈😈**Ɽǟɢǟռօʀӄɮð†**😈😈: 2.0\n\n"

pm_caption += "✨✨**¢нαииєℓ**✨✨: [ᴊᴏɪɴ](https://t.me/Raganork_Official)\n\n"

pm_caption += "⚜️⚜️**gяσυρ**⚜️⚜️: [ᴊᴏɪɴ](https://t.me/Raganork_bot_chat)\n\n"

pm_caption += "💫💫**ᴄᴜʀʀᴇɴᴛ ᴅɪʀᴇᴄᴛᴏʀʏ**💫💫: ᴋᴀʟɪ_ᴘᴀʀʀᴏᴛ_ᴛᴇʀᴍɪɴᴀʟ\n\n"

pm_caption += "🔥🔥**ᴅᴇᴠᴇʟᴏᴘᴇʀ 🔥🔥: [Raganork-Owner](https://t.me/HELLBOY_OP)\n\n"


pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/HELLBOY_OP)\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
