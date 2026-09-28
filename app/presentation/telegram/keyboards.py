from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_role_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Менеджер відправки"),
            ],
            [
                KeyboardButton(text="Адміністратор"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )