from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from config.database_config import get_db
from dao.book_dao import BookDao
from dto import book_dto

booksRouter = APIRouter(
    prefix="/books",
    tags=["books"]
)

bookDao = BookDao()


@booksRouter.get("/", response_model=List[book_dto.BookDto])
def findAll(db: Session = Depends(get_db)):
    return bookDao.findAll(db)


@booksRouter.get("/{book_id}", response_model=book_dto.BookDto)
def findOne(book_id: int, db: Session = Depends(get_db)):
    return bookDao.findOne(book_id, db)


@booksRouter.post("/", response_model=book_dto.BookDto)
def create(book: book_dto.BookDto, db: Session = Depends(get_db)):
    return bookDao.create(book, db)


@booksRouter.put("/{book_id}", response_model=book_dto.BookDto)
def update(book_id: int, book: book_dto.BookDto, db: Session = Depends(get_db)):
    return bookDao.update(book_id, book, db)


@booksRouter.delete("/{book_id}")
def delete(book_id: int, db: Session = Depends(get_db)):
    return bookDao.delete(book_id, db)
