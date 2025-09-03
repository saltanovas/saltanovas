from typing import Optional


class SpotifyException(Exception):
    """
    Base class for all Spotify exceptions.

    References:
        `Spotify API docs on Error Response
        <https://developer.spotify.com/documentation/web-api/concepts/api-calls#response-error>`_
    """

    def __init__(
            self,
            http_status_code: int,
            external_message: Optional[str],
    ):
        super().__init__(self.__str__())
        self.http_status_code = http_status_code
        self.external_message = external_message

    def __str__(self) -> str:
        return (
                f"SpotifyException [{self.http_status_code}]" +
                (f" | {self.external_message}" if self.external_message else "")
        )
