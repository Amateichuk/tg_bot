from langchain_core.documents import Document
from langchain_chroma import Chroma

from app.config import DB_PATH
from app.infrastructure.embeddings.ollama_embeddings import embeddings

print(DB_PATH)

def get_vector_store():
    return Chroma(
        collection_name="products",
        embedding_function=embeddings,
        persist_directory=DB_PATH
    )

def add_documents(products):
    """Додає Documents у Vector DB."""
    vector_store = get_vector_store()


    if not products:
        return

    documents = []

    for product in products:
        text = f"""
            Назва: {product['Назва']}
            Категорія: {product['Категорія']}
            Статус: {product['Статус']}
            Ціна: {product['Ціна']}
            Примітки: {product['Примітки']}
            """.strip()

        document = Document(
            page_content=text,
            metadata={
                "id": product["ID"],
                "name": product["Назва"],
                "category": product["Категорія"],
                "status": product["Статус"],
                "price": product["Ціна"],
            }
        )

        documents.append(document)

    vector_store.add_documents(documents)

    print(f"Додано у Vector DB: {len(documents)} товарів")

def search_document(query: str, k: int = 5):
    """Шукає найбільш релевантні документи."""
    vector_store = get_vector_store()

    return vector_store.similarity_search(
        query,
        k=k
    )

