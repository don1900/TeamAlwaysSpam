from .. import Don, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://telegra.ph/file/4cc84cabf3ee789d64ce0.jpg"

Don_Help = "🔥 Tᴇᴀᴍ Aʟᴡᴀʏꜱ 🔥\n\n"
 
Don_Help += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ʀɪᴢᴏᴇʟ x sᴘᴀᴍ__\n\n"

Don_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

Don_Help += f" `.bot` - to check ping\n `.robot` - to check bot alive/version (only main userbot will reply)\n .`reboot` - to restart all spam bots\n\n"
 
Don_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

Don_Help += f" `.bleave` - to leave public/private channel/groups\n\n"
 
Don_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

Don_Help += f" `.fuk` - to raid\n `.hardcore` - to active reply raid\n `.dhardcore` - to de-active reply raid\n `.bspam` - this cmd use for Normal spam\n `.bigbspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.dspam` - this cmd use for delay spam\n\n"


@Don.on(events.NewMessage(pattern=".bhelp"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("ᴄʀᴇᴀᴛᴏʀ", "https://t.me/Always_Don")
        ]
        ]
        )                      
