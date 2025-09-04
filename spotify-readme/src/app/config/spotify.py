import os
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SpotifyConfig:
    client_id: Optional[str] = os.getenv("SPOTIFY_CLIENT_ID")
    secret_id: Optional[str] = os.getenv("SPOTIFY_SECRET_ID")
    refresh_token: Optional[str] = os.getenv("SPOTIFY_REFRESH_TOKEN")
