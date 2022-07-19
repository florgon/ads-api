"""
    Ads API router.
    Provides API methods (routes) for working ads.
"""

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

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
async def method_ads_create(
    type: str, data: str, link: str, req: Request, db: Session = Depends(get_db)
) -> HTMLResponse | JSONResponse:
    """Creates new ad."""
    # TODO: type should be renamed.
    auth_data = query_auth_data_from_request(req)
    if type not in ("text", "image", "video"):
        return api_error(ApiErrorCode.API_INVALID_REQUEST, "Failed to create ad.")

    ad = crud.ad.create(db, owner_id=auth_data.user_id, ad_type=type, ad_data=data, ad_link=link)
    if ad:
        return api_success(serialize_ad(ad, in_list=False))
    return api_error(ApiErrorCode.API_UNKNOWN_ERROR, "Failed to create ad.")


@router.get("/ads.getViewBlock")
async def method_ads_get_view_block(
    req: Request, renderer: str | None = None, db: Session = Depends(get_db)
) -> HTMLResponse | JSONResponse:
    """Returns HTML/JS/CSS of the view block of the ad."""

    if renderer is None:
        renderer = "html"

    ad = crud.ad.get_random(db)

    if renderer == "html":
        return ads_view_block_html_renderer(ad=ad)
    elif renderer == "js":
        return ads_view_block_js_renderer(ad=ad)
    else:
        return api_error(
            ApiErrorCode.API_INVALID_REQUEST, "renderer must be 'html' or 'js'"
        )


@router.get("/ads.clickViewBlock")
async def method_ads_click_view_block(
    req: Request, aid: int, db: Session = Depends(get_db)
) -> HTMLResponse | JSONResponse:
    """Process analytics clicks for view block (ad) and redirect client (user) to the target resource page."""

    if not aid or aid <= 0:
        return api_error(ApiErrorCode.API_INVALID_REQUEST, "`aid` param is invalid!")
    ad = crud.ad.get_by_id(db, ad_id=aid)
    if not ad:
        return api_error(
            ApiErrorCode.API_INVALID_REQUEST, "Ad with this `aid` does not exist!"
        )

    return RedirectResponse(url=ad.link, status_code=307, headers=None)
