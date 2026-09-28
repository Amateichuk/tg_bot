from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    category: str
    status: str
    price: str
    notes: str