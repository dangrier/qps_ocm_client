from datetime import datetime, timedelta

from qps_ocm.model.Location import Location
from qps_ocm.provider.SecretsProvider import SecretsProvider
from qps_ocm.QPSOCMClient import QPSOCMClient

if __name__ == "__main__":
    client = QPSOCMClient(secrets_provider=SecretsProvider(), cached_locations=None)
    brisbane_region = client.get_location(957)
    print(brisbane_region)
    print(
        client.get_offences(
            datetime.now() - timedelta(days=90), datetime.now(), [brisbane_region]
        )
    )
