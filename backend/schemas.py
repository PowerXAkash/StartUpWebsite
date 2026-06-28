from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
    recommended_score: float
