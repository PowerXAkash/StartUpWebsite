from typing import Optional
from db.repository import create_item as save_item, get_item_by_id as load_item
from ai.predictor import AIPredictor
from backend.schemas import ItemCreate, ItemRead

predictor = AIPredictor()


def get_item(item_id: int) -> Optional[ItemRead]:
    record = load_item(item_id)
    if record is None:
        return None
    score = predictor.predict(record.description or record.name)
    return ItemRead(
        id=record.id,
        name=record.name,
        description=record.description,
        price=record.price,
        tax=record.tax,
        recommended_score=score,
    )


def create_item(item: ItemCreate) -> ItemRead:
    record = save_item(item)
    score = predictor.predict(item.description or item.name)
    return ItemRead(
        id=record.id,
        name=record.name,
        description=record.description,
        price=record.price,
        tax=record.tax,
        recommended_score=score,
    )
