from base import SpotifyException
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SpotifyAuthError:
    """
    Spotify Authentication Error data model.

    References:
        `Spotify API docs on Authentication Error Object
        <https://developer.spotify.com/documentation/web-api/concepts/api-calls#authentication-error-object>`_
    """
    error: str
    error_description: Optional[str] = None

    def __str__(self) -> str:
        return (
                f"SpotifyAuthError: {self.error}" +
                (f" | {self.error_description}" if self.error_description else "")
        )

    def __repr__(self) -> str:
        return (
            f"SpotifyAuthError("
            f"error={self.error!r}, "
            f"error_description={self.error_description!r})"
        )


class SpotifyAuthException(SpotifyException):
    """
    Raised when OAuth authentication flow fails.

    References:
        `Spotify API docs on Authentication Error Object
        <https://developer.spotify.com/documentation/web-api/concepts/api-calls#authentication-error-object>`_
    """

    def __init__(
            self,
            http_status_code: int,
            error: SpotifyAuthError,
            external_message: Optional[str],
    ):
        super().__init__(http_status_code, external_message)
        self.error = error.error
        self.error_description = error.error_description

    def __str__(self) -> str:
        return (
                f"SpotifyAuthException [{self.http_status_code}]: {self.error}" +
                (f" | {self.external_message}" if self.external_message else "")
        )

    def __repr__(self) -> str:
        return (
            f"SpotifyAuthException("
            f"http_status_code={self.http_status_code}, "
            f"error={self.error!r}, "
            f"external_message={self.external_message!r})"
        )
