from aiogram import Router
from aiogram.types import Message

from app.application.user_service import register_user

router = Router()


@router.message(lambda message: message.text =="Менеджер відправки")
async def manager_handler(message: Message):

    user = register_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        role="manager",
    )

    await message.answer(
        "✅ Ви зареєстровані як менеджер відправки.\n\n"
        "Ви будете отримувати повідомлення про нові замовлення."
    )

@router.message(lambda message: message.text == "Адміністратор")
async def admin_handler(message: Message):

    user = register_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        role="admin",
    )

    await message.answer(
        "✅ Ви зареєстровані як адміністратор."
    )