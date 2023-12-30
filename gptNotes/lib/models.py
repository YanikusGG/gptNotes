from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from flask_login import UserMixin

from .database import Base


class User(Base, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    notes = relationship("Note", back_populates="user")


class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    create_time = Column(TIMESTAMP, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)

    user = relationship("User", back_populates="notes")
