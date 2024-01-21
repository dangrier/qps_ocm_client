from pydantic import BaseModel
from base64 import standard_b64encode
from datetime import datetime, timezone, timedelta


class SecretsProvider(BaseModel):
    def get_api_key(self) -> str:
        # This isn't really a secret - it is included in the page source
        return "XoeWxarxOs1PKmZ2UkAnm8LfSjo29sei4P01NEbo"

    def get_basic_auth_secret(self) -> str:
        # Super basic auth secret as it turns out - get the current AEST timestamp in millis,
        # then character-wise reverse the string of numbers in the timestamp's integer representation
        return standard_b64encode(
            bytearray(str(int(datetime.now(timezone(timedelta(hours=10))).timestamp() * 1000))[::-1], "utf-8")
        ).decode("utf-8")
