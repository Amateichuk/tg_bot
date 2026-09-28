from typing import TypedDict

from app.models.order import OrderData


class OrderState(TypedDict, total=False):
    message: str
    id_order: bool
    order: OrderData
    count: int
    missing_field: str
    response: str

