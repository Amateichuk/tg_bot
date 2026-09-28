from app.infrastructure.vector_db.chroma import get_vector_store


def search_products(query: str):
    vector_store = get_vector_store()

    return vector_store.similarity_search(query, k=5)