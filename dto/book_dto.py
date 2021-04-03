from typing import Optional

from pydantic import BaseModel

from . import author_dto


class BookDto(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]
    author_id: int
    author: author_dto.AuthorDto
