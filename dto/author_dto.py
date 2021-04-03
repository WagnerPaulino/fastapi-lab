from pydantic import BaseModel


class AuthorDto(BaseModel):
    name: str
