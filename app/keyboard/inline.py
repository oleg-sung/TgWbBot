from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подписаться 🔥", callback_data="subscribe"),
        ]
    ]
)
