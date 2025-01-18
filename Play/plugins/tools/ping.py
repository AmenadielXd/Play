from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from Play import app
from Play.core.call import Anony
from Play.utils import bot_sys_stats
from Play.utils.decorators.language import language
from config import OWNER_ID

@app.on_message(filters.command(["mping"]) & filters.user(OWNER_ID))
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_text(
        text=_["ping_1"].format(app.mention),
    )
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping))
