from typing import Optional

from pydantic import BaseModel

from . import author_dto


class BookDtoIn(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]
    author_id: int

    class Config:
        orm_mode = True


class BookDtoOut(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]
    author_id: int
    author: Optional[author_dto.AuthorDtoIn]

    class Config:
        orm_mode = True
