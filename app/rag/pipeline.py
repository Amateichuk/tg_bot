# app/rag/pipeline.py

import logging

from app.infrastructure.llm.ollama import ask_llm
from app.rag.retriever import retrieve_documents
from app.rag.context_builder import build_context
from app.rag.prompt_manager import build_prompt
from app.rag.reranker import rerank_documents

logger = logging.getLogger(__name__)


async def ask_rag(question: str) -> str:
    logger.info("RAG started")

    # 1. Пошук продуктів
    documents = retrieve_documents(question, k=10)
    # logger.info("Retrieved %d documents", len(documents))

    # documents = await rerank_documents(
    #     question,
    #     documents,
    #     limit=5,
    # )

    # 2. Формування context
    context = build_context(documents)
    # context = "buu"

    # 3. Формування prompt
    prompt = build_prompt(question, context)

    # 4. Запит до LLM
    response = await ask_llm(prompt)

    logger.info("RAG finished")

    return response.content