import json
from datetime import datetime
from typing import Any, Dict, List, Optional

import blackboxprotobuf
import requests
from pydantic import BaseModel

from .adapter.Adapter import Adapter
from .model.Location import Location
from .model.Offence import Offence
from .provider.SecretsProvider import SecretsProvider


class QPSOCMClient(BaseModel):
    __DATE_FORMAT = "%m-%d-%Y"

    secrets_provider: SecretsProvider
    api_base_url: str = "https://4w0qhtalkj.execute-api.ap-southeast-2.amazonaws.com"
    common_headers: Dict[str, str] = {
            "authority": "4w0qhtalkj.execute-api.ap-southeast-2.amazonaws.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "origin": "https://qps-ocm.s3-ap-southeast-2.amazonaws.com",
            "referer": "https://qps-ocm.s3-ap-southeast-2.amazonaws.com/",
        }
    cached_locations: Optional[Dict[int, Location]]
    
    def __prepare_api_headers(self, requires_auth: bool = False) -> tuple[str, str]:
        h = self.common_headers.copy()
        if not requires_auth:
            return h
        h["x-api-key"] = self.secrets_provider.get_api_key()
        h["authorization"] = f"Basic {self.secrets_provider.get_basic_auth_secret()}"
        return h

    def __api_path(self, api_subpath: str) -> str:
        return f"{self.api_base_url}{api_subpath}"
    
    def __api_get_offences(self, date_from: datetime, date_to: datetime, locations: List[Location]) -> tuple[str, Any]:
        req = requests.get(
            url=self.__api_path(f"/dev/offences/{date_from.strftime(self.__DATE_FORMAT)}/{date_to.strftime(self.__DATE_FORMAT)}/{','.join([str(x.code) for x in locations])}"),
            headers=self.__prepare_api_headers(True),
        )

        try:
            message, _ = blackboxprotobuf.protobuf_to_json(req.content)
        except Exception as ex:
            print(ex)
            print(req.text)

        return list(map(Adapter.offence_from_blobject, json.loads(message)['4']['1']))
    
    def __api_get_locations(self) -> Dict[int, Location]:
        req = requests.get(
            url=self.__api_path("/dev/lut"),
            headers=self.__prepare_api_headers(False),
        )
        try:
            message, _ = blackboxprotobuf.protobuf_to_json(req.content)
        except Exception as ex:
            print(ex)
            print(req.text)
        return {x.code:x for x in map(Adapter.location_from_blobject, json.loads(message)['4']['1'])}
    
    def get_locations(self) -> Dict[int, Location]:
        if self.cached_locations != None:
            return self.cached_locations
        locations = self.__api_get_locations()
        self.cached_locations = locations
        return locations
    
    def get_location(self, code: int) -> Optional[Location]:
        return self.get_locations().get(code)

    def get_offences(self, date_from: datetime, date_to: datetime, locations: List[Location]) -> List[Offence]:
        data = self.__api_get_offences(date_from, date_to, locations)
        return data
