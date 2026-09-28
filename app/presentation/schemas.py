from pydantic import BaseModel

class BotResponse(BaseModel):
    text: str
    products: list[str] = []