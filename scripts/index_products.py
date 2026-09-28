from app.infrastructure.repositories.google_sheets import get_products
from app.infrastructure.vector_db.chroma import add_documents


def index_products():
    print("Починаємо індексацію...")

    products = get_products()

    print(f"Знайдено товарів: {len(products)}")

    add_documents(products)

    print("Товари додані у Vector DB")


if __name__ == "__main__":
    index_products()