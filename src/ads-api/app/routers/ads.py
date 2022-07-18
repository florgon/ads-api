"""
    Ads API router.
    Provides API methods (routes) for working ads.
"""

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse

# Etc.
from app.services.api.response import api_error, api_success, ApiErrorCode
from app.services.request import query_auth_data_from_request
from app.serializers.ad import serialize_ad

# Database.
from app.database import crud
from app.database.dependencies import get_db, Session

# Renderers.
from app.renderers.js import ads_view_block_js_renderer
from app.renderers.html import ads_view_block_html_renderer

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
        return ads_view_block_html_renderer(ad=ad)
    elif renderer == "js":
        return ads_view_block_js_renderer(ad=ad)
    else:
        return api_error(ApiErrorCode.API_INVALID_REQUEST, "renderer must be 'html' or 'js'")

