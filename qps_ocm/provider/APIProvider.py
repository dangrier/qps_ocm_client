from datetime import datetime
from functools import lru_cache
from typing import Any, Dict, List, MutableSet, Optional, OrderedDict

import geobuf
import requests
from pydantic import BaseModel

from ..adapter.Adapter import Adapter
from ..model.Location import Location
from ..model.Offence import Offence
from ..provider.SecretsProvider import SecretsProvider


class APIProvider(BaseModel):
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

    def __prepare_api_headers(self, requires_auth: bool = False) -> tuple[str, str]:
        h = self.common_headers.copy()
        if not requires_auth:
            return h
        h["x-api-key"] = self.secrets_provider.get_api_key()
        h["authorization"] = f"Basic {self.secrets_provider.get_basic_auth_secret()}"
        return h

    def __api_path(self, api_subpath: str) -> str:
        return f"{self.api_base_url}{api_subpath}"

    def get_offences(
        self, date_from: datetime, date_to: datetime, locations: MutableSet[Location]
    ) -> dict[str, Any] | OrderedDict | None:
        req = requests.get(
            url=self.__api_path(
                f"/dev/offences/{date_from.strftime(self.__DATE_FORMAT)}/{date_to.strftime(self.__DATE_FORMAT)}/{','.join([str(x.code) for x in locations])}"
            ),
            headers=self.__prepare_api_headers(True),
        )
        return geobuf.decode(req.content)

    def get_locations(self) -> dict[str, Any] | OrderedDict | None:
        req = requests.get(
            url=self.__api_path("/dev/lut"),
            headers=self.__prepare_api_headers(False),
        )
        return geobuf.decode(req.content)
