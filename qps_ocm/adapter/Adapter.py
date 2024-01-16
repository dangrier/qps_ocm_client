from datetime import datetime
from typing import Dict

from ..model.Location import Location
from ..model.Offence import Offence
from ..model.OffenceCategory import OffenceCategory


class Adapter:
    @staticmethod
    def location_from_blobject(blobject) -> Location:
        return Location(
            code=int(blobject['13'][0]['3']),
            type=blobject['13'][2]['1'],
            name=blobject['13'][1]['1'],
        )
    
    @staticmethod
    def offence_from_blobject(blobject) -> Offence:
        return Offence(
            start_time=datetime.fromtimestamp(int(blobject["13"][0]["3"])),
            category=OffenceCategory(int(blobject["13"][1]["3"])),
            location=int(blobject["13"][2]["3"]),
            coordinate=None,
        )