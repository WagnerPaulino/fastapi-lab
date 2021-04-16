from typing import Optional, List

from pydantic import BaseModel


class InnerAuthorBookDto(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]

    class Config:
        orm_mode = True


class AuthorDtoIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class AuthorDtoOut(BaseModel):
    id: Optional[int]
    name: str
    books: List[InnerAuthorBookDto]

    class Config:
        orm_mode = True
