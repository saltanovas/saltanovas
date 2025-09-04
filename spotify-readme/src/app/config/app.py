from dataclasses import dataclass
from server import ServerConfig
from spotify import SpotifyConfig
from ui import UIConfig


@dataclass(frozen=True)
class AppConfig:
    server: ServerConfig = ServerConfig()
    spotify: SpotifyConfig = SpotifyConfig()
    ui: UIConfig = UIConfig()
