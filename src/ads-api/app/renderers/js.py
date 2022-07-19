from fastapi.responses import JSONResponse
from app.database.models.ad import Ad
from app.services.api.response import api_success


def ads_view_block_js_renderer(ad: Ad) -> JSONResponse:
    if not ad:
        ad_id = 0
        ad_text = "Sorry, no ad was found for you! =("
        ad_link = "#"
    else:
        ad_id = ad.id
        ad_text = ad.text
        ad_link = f"https://ads.florgon.space/c?aid={ad_id}"

    return api_success({
        "view_block": {
            "type": "text",
            "data": ad_text,
            "link": ad_link
        },
        "payload": {
            "aid": ad_id
        }
    })