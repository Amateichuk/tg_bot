from pydantic import BaseModel, Field

class Delivery(BaseModel):
    city: str | None = None
    address: str | None = None
    payment_method: str | None = "Передплата"
    delivery_method: str | None = "Нова пошта"

class OrderItem(BaseModel):
    product_name: str | None = None
    quantity: str | int = "1"
    price: str | None = None

class OrderData(BaseModel):
    items: list[OrderItem] = Field(default_factory=list)

    full_name:str | None = None
    phone_number: str | None = None

    delivery: Delivery = Field(default_factory=Delivery)