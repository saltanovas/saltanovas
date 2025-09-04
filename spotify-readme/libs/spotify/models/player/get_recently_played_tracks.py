from dataclasses import dataclass
from typing import List, Optional, Dict


# --- Common ---
@dataclass(frozen=True)
class ExternalUrls:
    spotify: str


@dataclass(frozen=True)
class Image:
    url: str
    height: int
    width: int


@dataclass(frozen=True)
class Restrictions:
    reason: str


@dataclass(frozen=True)
class Artist:
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str


# --- Album ---
@dataclass(frozen=True)
class Album:
    album_type: str
    total_tracks: int
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    restrictions: Optional[Restrictions]
    type: str
    uri: str
    artists: List[Artist]


# --- Track ---
@dataclass(frozen=True)
class ExternalIds:
    isrc: Optional[str]
    ean: Optional[str]
    upc: Optional[str]


@dataclass(frozen=True)
class Track:
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrls
    href: str
    id: str
    is_playable: bool
    linked_from: Dict  # left generic (empty object in example)
    restrictions: Optional[Restrictions]
    name: str
    popularity: int
    preview_url: Optional[str]
    track_number: int
    type: str
    uri: str
    is_local: bool


# --- Context ---
@dataclass(frozen=True)
class Context:
    type: str
    href: str
    external_urls: ExternalUrls
    uri: str


# --- Item ---
@dataclass(frozen=True)
class PlayedItem:
    track: Track
    played_at: str
    context: Optional[Context]


# --- Cursors ---
@dataclass(frozen=True)
class Cursors:
    after: Optional[str]
    before: Optional[str]


# --- Root Response ---
@dataclass(frozen=True)
class GetRecentlyPlayedTracksResponse:
    href: str
    limit: int
    next: Optional[str]
    cursors: Cursors
    total: int
    items: List[PlayedItem]

@dataclass(frozen=True)
class GetRecentlyPlayedTracksRequest:
    limit: int | None = 20
    after: int | None = None
    before: int | None = None
