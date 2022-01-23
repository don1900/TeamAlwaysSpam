from .. import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@Don.on(events.NewMessage(pattern=r"\.bot"))
@Don2.on(events.NewMessage(pattern=r"\.bot"))
@Don3.on(events.NewMessage(pattern=r"\.bot"))
@Don4.on(events.NewMessage(pattern=r"\.bot"))
@Don5.on(events.NewMessage(pattern=r"\.bot"))
@Don6.on(events.NewMessage(pattern=r"\.bot"))
@Don7.on(events.NewMessage(pattern=r"\.bot"))
@Don8.on(events.NewMessage(pattern=r"\.bot"))
@Don9.on(events.NewMessage(pattern=r"\.bot"))
@Don10.on(events.NewMessage(pattern=r"\.bot"))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"░█▀▀█ ▒█░░░ ▒█░░▒█ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█\n▒█▄▄█ ▒█░░░ ▒█▒█▒█ ▒█▄▄█ ▒█▄▄▄█ ░▀▀▀▄▄\n▒█░▒█ ▒█▄▄█ ▒█▄▀▄█ ▒█░▒█ ░░▒█░░ ▒█▄▄▄█\n\n __PONG__ `{ms}` ᴍs")                       

