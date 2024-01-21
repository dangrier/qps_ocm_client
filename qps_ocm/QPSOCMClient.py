from datetime import datetime
from functools import lru_cache
from typing import Dict, List, MutableSet, Optional

from pydantic import BaseModel

from .adapter.Adapter import Adapter
from .model.Location import Location
from .model.LocationType import LocationType
from .model.Offence import Offence
from .provider.APIProvider import APIProvider
from .provider.SecretsProvider import SecretsProvider


class QPSOCMClient(BaseModel):
    api: APIProvider = APIProvider(
        secrets_provider=SecretsProvider(),
    )

    __HASH = 0

    def __hash__(self) -> int:
        return self.__HASH

    @lru_cache
    def get_locations(self) -> Dict[int, Location]:
        raw_data = self.api.get_locations()
        return Adapter.to_locations(raw_data["features"])

    def get_location(self, code: int) -> Optional[Location]:
        return self.get_locations().get(code)
    
    def get_location_by_name(self, type: LocationType, name: str) -> Optional[Location]:
        for l in self.get_locations().values():
            if l.type == type and l.name.lower() == name.lower():
                return l
        return None

    def get_offences(
        self, date_from: datetime, date_to: datetime, locations: MutableSet[Location]
    ) -> List[Offence]:
        raw_data = self.api.get_offences(date_from, date_to, locations)
        return Adapter.to_offences(raw_data["features"])
