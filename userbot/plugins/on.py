import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Raganork user"
PM_IMG = "https://telegra.ph/file/06dd3530fcd6649a4c756.jpg"
pm_caption = "This is **Raganork userbot !**\n\n"

pm_caption += f"✨Servant of my master \n  : {DEFAULTUSER} \n"

pm_caption += "✨**My Os**   ☞ ʟɪɴᴜx ᴍᴀɴᴅʀɪᴠᴀ  \n"

pm_caption += "**✨Mandriva Version**  : 1.07.3 \n"

pm_caption += "✨**Support Channel**   : [ᴊᴏɪɴ](https://t.me/Raganork_Official)\n"

pm_caption += "✨**Support group** : [ᴊᴏɪɴ](https://t.me/Raganork_bot_chat)\n"

pm_caption += "✨**Developer** :  [@HELLBOY_OP](https://t.me/Hellboy_Pikachu)  \n\n"

pm_caption += " [┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/Raganork_bot_chat)"

@borg.on(admin_cmd(pattern=r"on"))
async def amireallyalive(yes):
    chat = await yes.get_chat()
    await yes.delete()
    """ For .on command, check if I am on(alive) fire or not.  """
    await borg.send_file(yes.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
