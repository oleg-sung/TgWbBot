from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Получить информацию по товару"),
        ],
        [
            KeyboardButton(text="Остановить уведомления"),
        ],
        [
            KeyboardButton(text="Получить информацию из БД"),
        ],
    ],
    resize_keyboard=True,
)
