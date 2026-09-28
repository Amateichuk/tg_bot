import logging

from aiogram import Bot, Dispatcher

from app.presentation.telegram.handlers.start import router as start_router
from app.presentation.telegram.handlers.role import router as role_router
from app.presentation.telegram.handlers.chat_router import router as chat_router
from app.presentation.telegram.handlers.errors import router as errors_router

from app.config import BOT_TOKEN
from app.logging_config import setup_logging

setup_logging()

logger = logging.getLogger(__name__)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(role_router)
dp.include_router(chat_router)
dp.include_router(errors_router)

async def main():
    logger.info("Бот запускається")

    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())