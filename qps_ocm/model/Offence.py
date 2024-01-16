from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.coordinate import Coordinate

from .OffenceCategory import OffenceCategory


class Offence(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, use_enum_values=True)

    start_time: datetime
    category: OffenceCategory
    location: int
    coordinate: Optional[Coordinate]
