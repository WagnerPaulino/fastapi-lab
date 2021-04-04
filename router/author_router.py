from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from config.database_config import get_db
from dao.author_dao import AuthorDao
from dto import author_dto

authorsRouter = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

authorDao = AuthorDao()


@authorsRouter.get("/", response_model=List[author_dto.AuthorDtoOut])
def findAll(db: Session = Depends(get_db)):
    return authorDao.findAll(db)


@authorsRouter.get("/{author_id}", response_model=author_dto.AuthorDtoOut)
def findOne(author_id: int, db: Session = Depends(get_db)):
    return authorDao.findOne(author_id, db)


@authorsRouter.post("/", response_model=author_dto.AuthorDtoOut)
def create(author: author_dto.AuthorDtoIn, db: Session = Depends(get_db)):
    return authorDao.create(author, db)


@authorsRouter.put("/{author_id}", response_model=author_dto.AuthorDtoOut)
def update(author_id: int, author: author_dto.AuthorDtoIn, db: Session = Depends(get_db)):
    return authorDao.update(author_id, author, db)


@authorsRouter.delete("/{author_id}")
def delete(author_id: int, db: Session = Depends(get_db)):
    return authorDao.delete(author_id, db)
