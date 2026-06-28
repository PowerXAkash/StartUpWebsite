from typing import Optional
from db.models import Item as ItemModel
from db.session import SessionLocal
from backend.schemas import ItemCreate


def get_item_by_id(item_id: int) -> Optional[ItemModel]:
    with SessionLocal() as session:
        return session.get(ItemModel, item_id)


def create_item(item_create: ItemCreate) -> ItemModel:
    db_item = ItemModel(
        name=item_create.name,
        description=item_create.description,
        price=item_create.price,
        tax=item_create.tax,
    )
    with SessionLocal() as session:
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item
