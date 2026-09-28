import logging

from aiogram import Router
from aiogram.types import ErrorEvent

router = Router()

logger = logging.getLogger(__name__)


@router.error()
async def error_handler(event: ErrorEvent):
    logger.exception(
        "Помилка під час обробки повідомлення",
        exc_info=event.exception
    )

    if event.update.message:
        await event.update.message.answer(
            "⚠️ Виникла помилка. Спробуйте ще раз."
        )

    return True