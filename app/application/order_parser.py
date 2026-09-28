from app.infrastructure.llm.ollama import get_llm
from app.models.order import OrderData


def parse_order(message: str) -> OrderData:
    structured_llm = get_llm.with_structured_output(OrderData)

    return structured_llm.invoke(
        f"""
        Витягни дані замовлення з повідомлення користувача.

        Повідомлення:
        {message}
        """
    )