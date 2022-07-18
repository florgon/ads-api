"""
    Ads API router.
    Provides API methods (routes) for working ads.
"""

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse

from app.services.api.response import api_error, api_success, ApiErrorCode
from app.services.request import query_auth_data_from_request
from app.database import crud
from app.database.dependencies import get_db, Session
from app.serializers.ad import serialize_ad
from app.database.models.ad import Ad

router = APIRouter()


@router.get("/ads.create")
async def method_ads_create(text: str, req: Request, db: Session = Depends(get_db)) -> HTMLResponse | JSONResponse:
    """Returns HTML/JS/CSS of the view block of the ad. Should be called by JS-library on the client website."""
    auth_data = query_auth_data_from_request(req)
    ad = crud.ad.create(db, owner_id=auth_data.user_id, text=text)
    if ad:
      return api_success(serialize_ad(ad, in_list=False))  
    return api_error(ApiErrorCode.API_UNKNOWN_ERROR, "Failed to create ad.")


@router.get("/ads.getViewBlock")
async def method_ads_get_view_block(req: Request, renderer: str | None = None, db: Session = Depends(get_db)) -> HTMLResponse | JSONResponse:
    """Returns HTML/JS/CSS of the view block of the ad. Should be called by JS-library on the client website."""

    if renderer is None:
        renderer = "html"

    ad = crud.ad.get_random(db)

    if renderer == "html":
        return _ads_view_block_html_renderer(ad=ad)
    elif renderer == "js":
        return _ads_view_block_js_renderer(ad=ad)
    else:
        return api_error(ApiErrorCode.API_INVALID_REQUEST, "renderer must be 'html' or 'js'")


def _ads_view_block_js_renderer(ad: Ad) -> JSONResponse:
    if not ad:
        return api_success({
            "view_block": {
                "type": "text",
                "data": "Sorry, no ad was found for you! =("
            }
        })
    return api_success({
        "view_block": {
            "type": "text",
            "data": ad.text
        }
    })


def _ads_view_block_html_renderer(ad: Ad) -> HTMLResponse:
    if not ad:
        ad_text = "Sorry, no ad was found for you! =("
    else:
        ad_text = ad.text
    return HTMLResponse("""
        <html>
            <head>
                <style></style>
            </head>
            <body>
                <span>
                    {ad_text}
                </span>
            </body>
        </html>
    """.format(ad_text=ad_text))