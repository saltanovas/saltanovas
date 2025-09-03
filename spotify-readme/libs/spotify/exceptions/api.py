from base import SpotifyException
from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class SpotifyApiError:
    """
    Spotify API Error data model.

    References:
        `Spotify API docs on API Error Object
        <https://developer.spotify.com/documentation/web-api/concepts/api-calls#regular-error-object>`_
    """

    @dataclass(frozen=True)
    class Error:
        status: int
        message: str

        def __str__(self) -> str:
            return f"SpotifyError [{self.status}]: {self.message}"

        def __repr__(self) -> str:
            return (
                f"SpotifyError("
                f"status={self.status}, "
                f"message={self.message!r})"
            )

    error: Error

    def __str__(self) -> str:
        return str(self.error)

    def __repr__(self) -> str:
        return f"SpotifyApiError(error={self.error!r})"


class SpotifyApiException(SpotifyException):
    """
    Raised when API request fails.

    References:
        `Spotify API docs on API Error Object
        <https://developer.spotify.com/documentation/web-api/concepts/api-calls#regular-error-object>`_
    """

    def __init__(
            self,
            http_status_code: int,
            error: SpotifyApiError,
            external_message: Optional[str],
    ):
        super().__init__(http_status_code, external_message)
        self.error = error

    def __str__(self) -> str:
        return (
                f"SpotifyApiException [{self.http_status_code}]: {self.error}" +
                (f" | {self.external_message}" if self.external_message else "")
        )

    def __repr__(self) -> str:
        return (
            f"SpotifyApiException("
            f"http_status_code={self.http_status_code}, "
            f"error={self.error!r}, "
            f"external_message={self.external_message!r})"
        )
