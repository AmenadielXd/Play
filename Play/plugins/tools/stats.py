import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message,InputMediaVideo
from pytgcalls.__version__ import __version__ as pytgver

import config
import random
from Play import app
from Play.core.userbot import assistants
from Play.misc import SUDOERS, mongodb
from Play.plugins import ALL_MODULES
from Play.utils.database import get_served_chats, get_served_users, get_sudoers
from Play.utils.decorators.language import language, languageCB
from Play.utils.inline.stats import back_stats_buttons, stats_buttons
from config import OWNER_ID

@app.on_message(filters.command(["mstats"]) & filters.user(OWNER_ID))
async def stats_global(client, message: Message, _):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    random_image_url = random.choice(config.STATS_IMG_URL)  # Select a random image URL
    await message.reply(
        text=f'<a href="{random_image_url}"> 🍥</a> {_["gstats_2"].format(app.mention)}',
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("stats_back") & filters.user(OWNER_ID))
@languageCB
async def home_stats(client, CallbackQuery, _):
    upl = stats_buttons(_, True if CallbackQuery.from_user.id in SUDOERS else False)
    random_image_url = random.choice(config.STATS_IMG_URL)  # Select a random image URL
    await CallbackQuery.edit_message_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("TopOverall") & filters.user(OWNER_ID))
@languageCB
async def overall_stats(client, CallbackQuery, _):
    await CallbackQuery.answer()
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_3"].format(
        app.mention,
        len(assistants),
        len(BANNED_USERS),
        served_chats,
        served_users,
        len(ALL_MODULES),
        len(SUDOERS),
        config.AUTO_LEAVING_ASSISTANT,
        config.DURATION_LIMIT_MIN,
    )
    random_image_url = random.choice(config.STATS_IMG_URL)  # Select a random image URL
    await CallbackQuery.message.delete()
    await CallbackQuery.message.reply(text=f'<a href="{random_image_url}"> 🍥</a> {text}', reply_markup=upl)


@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def bot_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer(_["gstats_4"], show_alert=True)
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))

    # Collecting system stats
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"

    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"

    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    used = hdd.used / (1024.0**3)
    free = hdd.free / (1024.0**3)

    call = await mongodb.command("dbstats")
    datasize = call["dataSize"] / 1024
    storage = call["storageSize"] / 1024
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())

    text = _["gstats_5"].format(
        app.mention,
        len(ALL_MODULES),
        platform.system(),
        ram,
        p_core,
        t_core,
        cpu_freq,
        pyver.split()[0],
        pyrover,
        pytgver,
        str(total)[:4],
        str(used)[:4],
        str(free)[:4],
        served_chats,
        served_users,
        len(BANNED_USERS),
        len(await get_sudoers()),
        str(datasize)[:6],
        storage,
        call["collections"],
        call["objects"],
    )

    random_image_url = random.choice(config.STATS_IMG_URL)  # Select a random image URL
    await CallbackQuery.message.delete()
    await CallbackQuery.message.reply(text=f'<a href="{random_image_url}"> 🍥</a> {text}', reply_markup=upl)
