from abc import ABC, abstractmethod

from app.domain.models.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def get_products(self) -> list[Product]:
        pass