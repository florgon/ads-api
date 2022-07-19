from fastapi.responses import JSONResponse
from app.database.models.ad import Ad
from app.services.api.response import api_success


def ads_view_block_js_renderer(ad: Ad) -> JSONResponse:
    if not ad:
        return api_success({
            "view_block": {
                "type": "text",
                "data": "Sorry, no ad was found for you! =(",
                "link": "#"
            },
            "payload": {
                "aid": 0
            }
        })
    return api_success({
        "view_block": {
            "type": "text",
            "data": ad.text,
            "link": f"https://ads.florgon.space/c?aid={ad.id}"
        },
        "payload": {
            "aid": ad.id
        }
    })