from pydantic import BaseModel


class StatusDto(BaseModel):
    name: str
