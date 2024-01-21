from enum import StrEnum


class LocationType(StrEnum):
    SUBURB = "Suburb"
    POSTCODE = "Postcode"
    LOCAL_GOVERNMENT = "Local Government Area"
    NEIGHBOURHOOD_WATCH = "Neighbourhood Watch"
    POLICE_REGION = "QPS Region"
    POLICE_DISTRICT = "QPS District"
    POLICE_PATROL_GROUP = "QPS Patrol Group"
    POLICE_DIVISION = "QPS Division"
