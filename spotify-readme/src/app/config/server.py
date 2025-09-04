from dataclasses import dataclass

@dataclass(frozen=True)
class ServerConfig:
    port: int = 5001