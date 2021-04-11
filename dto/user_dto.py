from pydantic import BaseModel


class UserDtoIn(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserDtoOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
