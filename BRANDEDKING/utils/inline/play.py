import math

from pyrogram.types import InlineKeyboardButton

from BRANDEDKING.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    tgn = math.floor(percentage)
    if 0 < tgn <= 10:
        bar = "🏩▇▇▇▇▇▇▇▇▇"
    elif 10 < tgn < 20:
        bar = "▇💨▇▇▇▇▇▇▇▇"
    elif 20 <= tgn < 30:
        bar = "▇▇❣️▇▇▇▇▇▇▇"
    elif 30 <= tgn < 40:
        bar = "▇▇▇🍒▇▇▇▇▇▇"
    elif 40 <= tgn < 50:
        bar = "▇▇▇▇🦋▇▇▇▇▇"
    elif 50 <= tgn < 60:
        bar = "▇▇▇▇▇🌷▇▇▇▇"
    elif 60 <= tgn < 70:
        bar = "▇▇▇▇▇▇♦️▇▇▇"
    elif 70 <= tgn < 80:
        bar = "▇▇▇▇▇▇▇🎀▇▇"
    elif 80 <= tgn < 95:
        bar = "▇▇▇▇▇▇▇▇💌▇"
    else:
        bar = "▇▇▇▇▇▇▇▇▇❤‍🩹"
    buttons = [
        [
            InlineKeyboardButton(text="", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌼 ᴘʟᴀʏʟɪsᴛs", callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="✨ 𝐎ωиєя ⏎", url="https://t.me/L2R_KING0",
            ),
        ],
        [
            InlineKeyboardButton(
                 text="💮︎ ᴄᴘᴀɴɴᴇʟ", url="https://t.me/ALL_QUIZ_TAME",
            ),
            InlineKeyboardButton(
                text="⛩️ Gʀᴏᴜᴘꨄ︎ ⛩️", url="https://t.me/MUSICBOT_OWNER",
            ),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="🌼 ᴘʟᴀʏʟɪsᴛs", callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="✨ 𝐎ωиєя ⏎", url="https://t.me/L2R_KING0",
            ),
        ],
        [
            InlineKeyboardButton(
                 text="💮︎ ᴄᴘᴀɴɴᴇʟ", url="https://t.me/ALL_QUIZ_TAME",
            ),
            InlineKeyboardButton(
                text="⛩️ Gʀᴏᴜᴘꨄ︎ ⛩️", url="https://t.me/MUSICBOT_OWNER",
            ),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
