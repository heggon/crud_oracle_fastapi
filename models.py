from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Identity, Table, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('users_seq', start=1), primary_key=True, index=True)
    email = Column(String(length=500), unique=True, index=True)
    hashed_password = Column(String(length=500))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, Sequence('items_seq', start=1), primary_key=True, index=True)
    title = Column(String(length=500), index=True)
    description = Column(String(length=500), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")