from sqlalchemy.orm import Session

from domain.models import Book
from dto.book_dto import BookDto


class BookDao:
    def findAll(self, db: Session):
        return db.query(Book).all()

    def findOne(self, book_id: int, db: Session):
        return db.query(Book).filter(Book.id == book_id).first()

    def create(self, book: BookDto, db: Session):
        db_book = Book(**book.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    def update(self, book_id: int, book: BookDto, db: Session):
        db.query(Book).filter(Book.id == book_id).update(**book.dict())
        db.commit()
        return book

    def delete(self, book_id: int, db: Session):
        db.query(Book).filter(Book.id == book_id).delete()
        db.commit()
