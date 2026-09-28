from langchain_core.documents import Document
from app.infrastructure.llm.ollama import ask_llm


async def rerank_documents(
    question: str,
    documents: list[Document],
    limit: int = 5,
) -> list[Document]:

    if not documents:
        return []

    products = "\n\n".join(
        f"ID: {i}\n{document.page_content}"
        for i, document in enumerate(documents)
    )

    prompt = f"""
        Ти — система reranking для пошуку товарів.
        
        Питання користувача:
        {question}
        
        Товари:
        {products}
        
        Вибери {limit} найбільш релевантних товарів.
        
        Поверни ТІЛЬКИ номери товарів через кому.
        Наприклад:
        2, 0, 4
        """

    response = await ask_llm(prompt)

    try:
        indexes = [
            int(index.strip())
            for index in response.content.split(",")
        ]

        indexes = [
            index for index in indexes
            if 0 <= index < len(documents)
        ]

        return [documents[index] for index in indexes[:limit]]

    except (ValueError, AttributeError):
        return documents[:limit]