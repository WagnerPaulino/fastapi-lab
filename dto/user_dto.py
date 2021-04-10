from typing import Optional

from pydantic import BaseModel


class UserDtoIn(BaseModel):
    id: Optional[int]
    username: str
    password: str

    class Config:
        orm_mode = True


class UserDtoOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
