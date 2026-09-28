from langchain_ollama import ChatOllama

from app.config import LLM_MODEL


def get_llm() -> ChatOllama:
    return ChatOllama(
        model=LLM_MODEL,
        temperature=0,
    )


async def ask_llm(prompt: str):
    llm = get_llm()
    return await llm.ainvoke(prompt)