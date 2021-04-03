from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from config.database_config import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "book"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, unique=True, index=True)
    description: str = Column(String, nullable=True)
    price: float = Column(Float, nullable=False)
    tax: float = Column(Float, nullable=True)
    author_id: int = Column(Integer, ForeignKey("author.id"))
    author = relationship("Author", back_populates="books")
