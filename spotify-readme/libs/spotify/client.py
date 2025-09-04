from base64 import b64encode

import requests
from typing import Any, Dict
from ..exceptions import api as exception
from ..config import SpotifyConfig

def getAuth(config: SpotifyConfig) -> str:
    return b64encode(f"{config.client_id}:{config.secret_id}".encode()).decode("ascii")

class SpotifyClient:
    def __init__(self, config: SpotifyConfig) -> None:
        self.config = config

    def get_access_token(self) -> Dict[str, Any]:
        return requests.post(
            url=self.config.token_url,
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.config.refresh_token,
            },
            headers={"Authorization": f"Basic {getAuth()}"}
        ).json()

    # https://developer.spotify.com/documentation/web-api/reference/get-the-users-currently-playing-track
    def get_currently_playing_track(self, token) -> Dict[str, Any]:
        return self._get(token, self.config.currently_playing_track_url)

    def get_recently_played_tracks(self, token) -> Dict[str, Any]:
        return self._get(token, self.config.recently_played_tracks_url)

    def _get(self, token, url: str) -> Dict[str, Any]:
        try:
            response = requests.get(
                url=url,
                headers={"Authorization": f"Bearer {token}"},
                timeout=5
            )
        except requests.Timeout as e:
            raise exception.SpotifyApiException(
                http_status_code=408,
                error=None,
                external_message="Request timeout"
            )

        except requests.ConnectionError:
            raise exception.SpotifyApiException(
                http_status_code=503,
                error=None,
                external_message="Connection failed"
            )

        except requests.RequestException as e:
            raise exception.SpotifyApiException(
                http_status_code=500,
                error=None,
                external_message=f"Request has failed on the server side: {str(e)}"
            )

        try:
            return response.json()
        except ValueError:
            raise exception.SpotifyApiException(
                http_status_code=response.status_code,
                error=None,
                external_message="Response content is not a valid JSON"
            )
