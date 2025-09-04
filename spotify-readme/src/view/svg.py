from flask import Blueprint, route, request, Response

spotify_badge_bp = Blueprint("spotify_badges", __name__, url_prefix="/badges/spotify")


class SVGView:
    def __init__(self, svg_content: str):
        self.svg_content = svg_content

    @spotify_badge_bp.route(".<fmt>", methods=["GET"])
    def badge(self, provider, fmt="svg"):

        theme = next((t for t in THEMES if t.lower() == request.args.get('theme')), "light")

        try:
            data = get(SPOTIFY_CURRENTLY_PLAYING_URL)
        except Exception:
            data = get(SPOTIFY_RECENTLY_PLAYED_URL)

        return Response(
            response=makeSVG(data, theme),
            status=200,
            mimetype="image/svg+xml",
            headers={
                "Cache-Control": "s-maxage=1"
            }
        )
