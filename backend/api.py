from fastapi import APIRouter, HTTPException
from typing import Optional
from backend.service import ItemCreate, ItemRead, get_item, create_item

router = APIRouter(prefix="/api", tags=["api"])

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/items/{item_id}", response_model=ItemRead)
async def read_item(item_id: int, q: Optional[str] = None):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/items", response_model=ItemRead)
async def create_item_endpoint(item: ItemCreate):
    return create_item(item)
