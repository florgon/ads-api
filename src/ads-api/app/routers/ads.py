"""
    Ads API router.
    Provides API methods (routes) for working ads.
"""

from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

from app.services.api.response import api_error, api_success, ApiErrorCode

router = APIRouter()


@router.get("/ads.getViewBlock")
async def method_ads_get_view_block(renderer: str | None = None) -> HTMLResponse | JSONResponse:
    """Returns HTML/JS/CSS of the view block of the ad. Should be called by JS-library on the client website."""

    if renderer is None:
        renderer = "html"

    if renderer == "html":
        return ads_view_block_html_renderer()
    elif renderer == "js":
        return ads_view_block_js_renderer()
    else:
        return api_error(ApiErrorCode.API_INVALID_REQUEST, "renderer must be 'html' or 'js'")


def ads_view_block_js_renderer() -> JSONResponse:
    return api_success({
        "view_block": {
            "type": "text",
            "data": "Welcome to the Florgon Ads."
        }
    })


def ads_view_block_html_renderer() -> HTMLResponse:
    return HTMLResponse("""
        <html>
            <head>
                <style></style>
            </head>
            <body>
                Welcome to the Florgon Ads.
            </body>
        </html>
    """)