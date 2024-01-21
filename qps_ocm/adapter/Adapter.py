from datetime import datetime

from pydantic_extra_types.coordinate import Coordinate

from ..model.Location import Location
from ..model.LocationType import LocationType
from ..model.Offence import Offence
from ..model.OffenceCategory import OffenceCategory


class Adapter:
    @staticmethod
    def to_locations(geobuf_features):
        return {
            feature["properties"]["objectid"]: Location(
                code=feature["properties"]["objectid"],
                type=LocationType(feature["properties"]["type"]),
                name=feature["properties"]["label"],
            )
            for feature in geobuf_features
        }

    @staticmethod
    def to_offences(geobuf_features):
        return [
            Offence(
                start_time=datetime.fromtimestamp(feature["properties"]["date"]),
                category=OffenceCategory(feature["properties"]["o_code"]),
                coordinate=Coordinate(
                    latitude=feature["geometry"]["coordinates"][1],
                    longitude=feature["geometry"]["coordinates"][0],
                ),
                location=feature["properties"]["l_code"],
            )
            for feature in geobuf_features
        ]
