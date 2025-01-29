import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", None))
OWNER_ID = int(getenv("OWNER_ID", 6502950481))
BOT_NAME = getenv("BOT_NAME", "Nova UI")
BOT_USERNAME = getenv("BOT_USERNAME", "novauibot")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/none")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/none")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AmenadielXd/AlexPlay",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 3000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6f3a17d843444c0397ef739342758b46")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c69244c18a9743bf9fa96efd95dd93f1")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))


STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/dsg8dl.mp4"
STATS_IMG_URL = [ "https://unitedcamps.in/Images/file_5843.jpg",
"https://unitedcamps.in/Images/file_10524.jpg",
"https://unitedcamps.in/Images/file_10523.jpg",
"https://unitedcamps.in/Images/file_10522.jpg",
"https://unitedcamps.in/Images/file_10521.jpg",
"https://unitedcamps.in/Images/file_10520.jpg",
"https://unitedcamps.in/Images/file_10519.jpg",
"https://unitedcamps.in/Images/file_10518.jpg",
"https://unitedcamps.in/Images/file_10517.jpg",
"https://unitedcamps.in/Images/file_10516.jpg",
"https://unitedcamps.in/Images/file_10515.jpg",
"https://unitedcamps.in/Images/file_10514.jpg", ]
TELEGRAM_AUDIO_URL = "https://unitedcamps.in/Images/file_5654.jpg"
TELEGRAM_VIDEO_URL = "https://unitedcamps.in/Images/file_5654.jpg"
STREAM_IMG_URL = "https://unitedcamps.in/Images/file_5654.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://unitedcamps.in/Images/file_5843.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://unitedcamps.in/Images/file_5903.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://unitedcamps.in/Images/file_5903.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://unitedcamps.in/Images/file_5903.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
