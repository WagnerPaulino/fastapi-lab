from typing import Optional

from pydantic import BaseModel


class AuthorDtoIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class AuthorDtoOut(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True
