from typing import Optional

from pydantic import BaseModel


class InnerBookAuthorDto(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


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
    author: InnerBookAuthorDto

    class Config:
        orm_mode = True
