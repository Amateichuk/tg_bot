from app.graph.state import OrderState
from app.models.order import OrderData
from app.application.order_parser import parse_order
from app.models.order import Delivery


def extract_order(state: OrderState) -> OrderState:
    message = state["message"]

    new_order = parse_order(message)

    old_order = state.get('order')

    if old_order:
    # Оновлюємо тільки ті поля,
    # які реально знайшли в новому повідомленні

        if new_order.full_name:
            old_order.full_name = new_order.full_name

        if new_order.phone_number:
            old_order.phone_number = new_order.phone_number

        if new_order.delivery:
            if not old_order.delivery:
                old_order.delivery = Delivery()

            if new_order.delivery.city:
                old_order.delivery.city = new_order.delivery.city

            if new_order.delivery.address:
                old_order.delivery.address = new_order.delivery.address

            if new_order.delivery.delivery_method:
                old_order.delivery.delivery_method = new_order.delivery.delivery_method

            if new_order.delivery.payment_method:
                old_order.delivery.payment_method = new_order.delivery.payment_method

    order = old_order

    return {
        **state,
        "order": order,
    }

def check_order(state: OrderState) -> OrderState:
    order = state['order']

    if not order.items:
        return {
            **state,
            "missing_field": "product",
            "response": "Який товар ви хочете добавити?"
        }

    for item in order.items:
        if not item.product_name:
            return {
                **state,
                "missing_field": "product",
                "response": "Вкажіть, будь ласка, назву товару."
            }

    if not order.full_name:
        return {
            **state,
            "missing_field": "full_name",
            "response": "Вкажіть, будь ласка, ім'я та прізвище."
        }

    if not order.phone_number:
        return {
            **state,
            "missing_field": "phone_number",
            "response": "Вкажіть, будь ласка, номер телефону",
        }

    # Місто
    if not order.delivery.city:
        return {
            **state,
            "missing_field": "city",
            "response": "Вкажіть, будь ласка, місто доставки.",
        }

    # Адреса / відділення
    if not order.delivery.address:
        return {
            **state,
            "missing_field": "address",
            "response": "Вкажіть, будь ласка, відділення або адресу доставки.",
        }

    return {
        **state,
        "order": order,
    }


def has_delivery(delivery) -> bool:
    if not delivery:
        return False

    return bool(
        delivery.city
        or delivery.branch
        or delivery.address
    )


def is_order(order: OrderData) -> bool:
    return bool(
        order.full_name
        or order.phone_number
        or has_delivery(order.delivery)
    )


def classify_message(state: OrderState) -> OrderState:
    order = state["order"]

    return {
        **state,
        "is_order": is_order(order),
    }


def route_message(state: OrderState):
    if state["is_order"]:
        return "order"

    return "question"