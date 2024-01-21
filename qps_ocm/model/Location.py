from pydantic import BaseModel

from .LocationType import LocationType


class Location(BaseModel):
    code: int
    type: LocationType
    name: str
