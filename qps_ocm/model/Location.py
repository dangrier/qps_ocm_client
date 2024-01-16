from pydantic import BaseModel

class Location(BaseModel):
    code: int
    type: str
    name: str
