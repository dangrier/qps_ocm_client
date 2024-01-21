from collections import OrderedDict
from datetime import datetime, timedelta

from qps_ocm.QPSOCMClient import QPSOCMClient
from qps_ocm.model.LocationType import LocationType
from qps_ocm.model.OffenceCategory import OffenceCategory

if __name__ == "__main__":
    client = QPSOCMClient()
    area_type = LocationType(input("Which type of area will you be searching for offences in [Suburb]? ") or "Suburb")

    suburb_name = input(f"Which {area_type} do you want to search for offences in [Brisbane City]? ") or "Brisbane City"
    search_area = client.get_location_by_name(area_type, suburb_name)

    daysago = int(input("Search from how many days ago [90]? ") or 90)
    offences = client.get_offences(
        datetime.now() - timedelta(days=90),
        datetime.now(),
        [search_area],
    )

    print(f"\nThere were {len(offences)} offences in {search_area.name} ({search_area.type}) in the last {daysago} days:")
    categorical_statistics = {}
    for offence in offences:
        current = categorical_statistics.get(offence.category)
        if current:
            current += 1
        else:
            current = 1
        categorical_statistics[offence.category] = current

    for k, v in sorted(categorical_statistics.items(), key=lambda x:x[1], reverse=True):
        print(f"{OffenceCategory(k)}: {v}")
        