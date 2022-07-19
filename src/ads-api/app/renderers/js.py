from fastapi.responses import JSONResponse
from app.database.models.ad import Ad
from app.services.api.response import api_success
from app.config import get_settings


def ads_view_block_js_renderer(ad: Ad) -> JSONResponse:
    if not ad:
        ad_id = 0
        ad_data = "Sorry, no ad was found for you! =("
        ad_type = "text"
        ad_link = "#"
    else:
        ad_id = ad.id
        ad_data = ad.data
        ad_type = ad.type
        ad_link = f"{get_settings().ad_gateway_url}?aid={ad_id}"

    return api_success(
        {
            "view_block": {"type": ad_type, "data": ad_data, "link": ad_link},
            "payload": {"aid": ad_id},
        }
    )
