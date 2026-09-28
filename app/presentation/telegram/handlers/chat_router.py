import logging

from aiogram import Router
from aiogram.types import Message

from app.config import USE_AI
from app.application.chat_service import get_simple_response

router = Router()

logger = logging.getLogger(__name__)


@router.message()
async def message_handler(message: Message):
    logger.info("CHAT ID: %s", message.chat.id)

    if USE_AI:
    # if False:
        logger.info("2. AI MODE")

        from app.rag.pipeline import ask_rag
        logger.info("2.2 AFTER IMPORT")

        if not message.text:
            await message.answer("Будь ласка, напишіть текстове повідомлення.")
            return


        answer = await ask_rag(message.text)
        answer += " [AI]"

        logger.info("4. AFTER RAG")
    else:
        if not message.text:
            await message.answer("Будь ласка, напишіть текстове повідомлення.")
            return

        answer = get_simple_response(message.text)
        answer += " [SIMPLE]"

    await message.answer(answer)