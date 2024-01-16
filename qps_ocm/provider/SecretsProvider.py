from pydantic import BaseModel
from base64 import standard_b64encode
from datetime import datetime, timezone, timedelta


class SecretsProvider(BaseModel):
    def get_api_key(self) -> str:
        return "XoeWxarxOs1PKmZ2UkAnm8LfSjo29sei4P01NEbo"

    def get_basic_auth_secret(self) -> str:
        return standard_b64encode(
            bytearray(str(int(datetime.now(timezone(timedelta(hours=10))).timestamp() * 1000))[::-1], "utf-8")
        ).decode("utf-8")
