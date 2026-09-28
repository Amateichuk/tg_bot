from aiogram import Bot

from app.application.user_service import get_manager_users

async def notify_manager(
    bot: Bot,
    message: str,
) -> None:

    managers = get_manager_users()

    for manager in managers:
        await bot.send_message(
            manager['telegram_id'],
            message,
        )