from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    username = Column(String(100), index=True)
    phone = Column(String(20), unique=True, index=True)
    avatar = Column(String(100))
    hashed_password = Column(String(200), nullable=False)
    state = Column(Integer, index=True, default=1)
    role = Column(Integer, index=True, default=1)
    is_deleted = Column(Boolean(), default=False)
    last_login_datetime = Column(DateTime, nullable=True)
    create_datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    update_datetime = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
    items = relationship("Item", back_populates="owner")