import os
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class RedisConfig:
    url: Optional[str] = os.getenv("REDIS_URL")
