from .. import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://telegra.ph/file/4cc84cabf3ee789d64ce0.jpg"

Don_Help = "π₯ Tα΄α΄α΄ AΚα΄‘α΄Κκ± π₯\n\n"
 

Don_Help += f" β§ πππ΄ππ±πΎπ π²πΌπ³π β§\n\n"

Don_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version \n .`reboot` - to restart all spam bots\n\n"
 
Don_Help += f" β§ π»π΄π°ππ΄ π²πΌπ³ β§\n\n"

Don_Help += f" `.bleave` - to leave public/private channel/groups\n\n"
 
Don_Help += f" β§ ππΏπ°πΌ π²πΌπ³π β§\n\n"

Don_Help += f" `.fuk` - to raid\n `.hardcore` - to active reply raid\n `.dhardcore` - to de-active reply raid\n `.bspam` - this cmd use for Normal spam\n `.bigbspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.dspam` - this cmd use for delay spam\n\n"


@Don.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      

@Don2.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don2.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      
  
@Don3.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don3.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      

@Don4.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don4.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      
  
@Don5.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don5.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      

@Don6.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don6.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      
    
@Don7.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don7.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      
    
@Don8.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don8.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      
    
@Don9.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don9.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      
   
@Don10.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Don10.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Don_Help,
                                  buttons=[
        [
        Button.url("α΄Κα΄α΄α΄α΄Κ", "https://t.me/Always_Don")
        ]
        ]
        )                      
