from sqlalchemy import Column, Integer, String, Float, Text
from db.session import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    tax = Column(Float)
