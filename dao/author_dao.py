from sqlalchemy.orm import Session

from domain.models import Author
from dto.author_dto import AuthorDtoIn


class AuthorDao:
    def findAll(self, db: Session):
        return db.query(Author).all()

    def findOne(self, book_id: int, db: Session):
        return db.query(Author).filter(Author.id == book_id).first()

    def create(self, author: AuthorDtoIn, db: Session):
        db_book = Author(**author.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    def update(self, author_id: int, author: AuthorDtoIn, db: Session):
        db.query(Author).filter(Author.id == author_id).update(author.dict(), synchronize_session=False)
        db.commit()
        return author

    def delete(self, author_id: int, db: Session):
        db.query(Author).filter(Author.id == author_id).delete()
        db.commit()
