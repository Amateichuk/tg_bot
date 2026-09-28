from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.presentation.telegram.keyboards import get_role_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Вітаю!\n\n"
        "Оберіть вашу роль:",
        reply_markup=get_role_keyboard(),
    )