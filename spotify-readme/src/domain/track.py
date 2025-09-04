from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Artist:
    name: str
    uri: str


@dataclass(frozen=True)
class Song:
    name: str
    uri: str
    image_url: Optional[str]
    is_playing: bool = False


@dataclass(frozen=True)
class Track:
    artist: Artist
    song: Song
