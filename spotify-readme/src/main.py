from dotenv import load_dotenv, find_dotenv
from flask import Flask
from config import AppConfig
from services.client import SpotifyClient
from view.svg import spotify_badge_bp

app = Flask(__name__)

if __name__ == "__main__":
    load_dotenv(find_dotenv())

    client = SpotifyClient(AppConfig.spotify)

    app = Flask(__name__)
    app.register_blueprint(spotify_badge_bp)
    app.run(host="0.0.0.0", debug=True, port=AppConfig.server.port)
