# ©️ @SACHIN_OWNER || @V_VIP_OWNER 
from telethon import __version__, events, Button
import asyncio
import sys
import heroku3
from time import time
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon import events, version, Button
from telethon.tl.custom import button
from os import execl, getenv
from telethon.tl.functions.channels import LeaveChannelRequest

pongg = " ғ ᴀ ᴅ ᴇ ᴅ "
PIC = "https://files.catbox.moe/kjsdy6.jpg"
Alivemsg = "𓆩𝔽𝔸𝔻𝔼𝔻 ⚡ ℍ𝕌𓆪  ʜᴇʀᴇ"

TEXT = f"▬▭▬▭▬▭▬▭▬▭▬▭▬▭\nㅤㅤ❖ | 𓆩𝔽𝔸𝔻𝔼𝔻 ⚡ ℍ𝕌𓆪  | ❖\n▬▭▬▭▬▭▬▭▬▭▬▭▬▭\n❖ ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ : `4.15.7` \n❖ ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ : `M4.0` \n❖ sᴜᴘᴘᴏʀᴛ : [𓆩𝔽𝔸𝔻𝔼𝔻 ⚡ ℍ𝕌𓆪]https://t.me/+qYRBJgZsARpkNWJl)\n❖ ᴄʜᴀɴɴᴇʟ : [🕷F A D E D 🕸](https://t.me/+2H35U0oVDEIwMGEx)\n❖ ᴏᴡɴᴇʀ : [ ғᴀᴅᴇᴅ ʜᴜ ⚡  ](t.me/ll_FADED_HU_ll)\n▬▭▬▭▬▭▬▭▬▭▬▭▬▭"
                                  
@X1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  PIC,
                                  caption=TEXT,
                                  buttons=[
        [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/+2H35U0oVDEIwMGEx"),
        Button.url("• ꜱᴜᴘᴘᴏʀᴛ •", "https://t.me/+amibVQYuMGw3ZDY1")
        ],
        ]
        )
    
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

@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(KEX):
    if KEX.sender_id == SUDO_USERS:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await KEX.reply(
                KEX.chat_id,
                "ꜰɪʀꜱᴛ ꜱᴇᴛ ᴛʜᴇꜱᴇ ᴠᴀʀꜱ :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await KEX.reply(
                "ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴋᴇʏ ᴀɴᴅ ᴀᴘᴘ ɴᴀᴍᴇ ᴀʀᴇ ᴄᴏɴꜰɪɢᴜᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ"
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await KEX.reply(f"ꜰᴇᴛᴄʜʜɪɴɢ ʟᴏɢꜱ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...")
    
        with open("Logs.txt", "w") as logfile:
            logfile.write("ғᴀᴅᴇᴅ 🍷 [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(KEX.chat_id, "ʟᴏɢꜱ.ᴛxᴛ", caption=f"**ᴅᴇsᴛʀᴏʏᴇʀ ʙᴏᴛ ʟᴏɢꜱ 🍷**\n  » **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ ⌛:** `{ms} ꜱᴇᴄᴏɴᴅꜱ`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"**ᴇʀᴏᴏʀ:** {str(e)}")

    elif KEX.sender_id == OWNER_ID:
        await KEX.reply("❖ ɴᴏ ᴏɴʟʏ ғᴀᴅᴇᴅ ᴅᴀᴅᴅʏ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id == OWNER_ID:

        if len(e.text) > 7:
            event = await e.reply("❖ ғʜɪʀ ᴀᴀᴜɴɢᴀ ᴍᴀᴀ ᴄʜᴏᴅɴᴇ...")
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
                await event.edit(str(e))
        else:
             if e.is_private:
                  alt = f"**❖ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴛʜɪꜱ ʜᴇʀᴇ !!**\n\n❖ {hl}ʟᴇᴀᴠᴇ : ᴛʏᴘᴇ ᴛʜɪꜱ ɪɴ ɢʀᴏᴜᴘ"
                  await e.reply(alt)
             else:
                  event = await e.reply("❖ ғʜɪʀ ᴀᴀᴜɴɢᴀ ᴍᴀᴀ ᴄʜᴏᴅɴᴇ...")
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(str(e))        

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        KEX = await e.reply(f"❖ | 𝔽𝔸𝔻𝔼𝔻 ⚡ ℍ𝕌 | ❖")
        end = datetime.now()
        mp = (end - start).microseconds / 10000
        await KEX.edit(f"[🍹] 𝘍𝘈𝘋𝘌𝘋 ✗ 𝘋𝘈𝘋𝘋𝘠\n[🏓] 𝘛𝘏𝘈𝘓𝘈 ✗ 𝘍𝘠𝘛𝘌𝘙\n[⚡] 𝘙𝘌𝘈𝘋𝘠 𝘛𝘖 𝘍𝘊𝘒\n❖ ᴘɪɴɢ pong `{mp} ᴍꜱ`") 

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"❖ ғᴀᴅᴇᴅ ᴋᴀ ᴇᴋ ᴏʀ ʙᴇᴛᴀ ᴀᴅᴅ ʜᴏʀʜᴀ ʜ...")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("❖ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"❖ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ғᴀᴅᴇᴅ ᴋɪᴅ !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"❖ **ㅤ𝘍𝘈𝘋𝘌𝘋 𝘒𝘐 𝘈𝘜𝘓𝘈𝘋 **\n❖ ɪᴅ - `{target}`\n❖ ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("❖ ꜱᴏʀʀʏ, ᴏɴʟʏ ғᴀᴅᴇᴅ ᴅᴀᴅᴅʏ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")        

@X1.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"❖ ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)
