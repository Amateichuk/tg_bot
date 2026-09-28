# app/rag/retriever.py

from app.infrastructure.vector_db.chroma import search_document


def retrieve_documents(question: str, k: int = 5):
    return search_document(question, k)