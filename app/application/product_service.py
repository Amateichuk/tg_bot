from app.infrastructure.repositories.google_sheets import get_products


def get_all_products() -> list[dict]:
    return get_products()


def get_available_products() -> list[dict]:
    products = get_products()

    return [
        product
        for product in products
        if product["Статус"] == "В наявності"
    ]


def find_product_by_id(product_id: int) -> dict | None:
    products = get_products()

    for product in products:
        if int(product["ID"]) == product_id:
            return product

    return None