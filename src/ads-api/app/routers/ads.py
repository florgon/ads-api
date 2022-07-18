"""
    Ads API router.
    Provides API methods (routes) for working ads.
"""

from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/ads.getViewBlock")
async def method_ads_get_view_block(client_id: int = 0) -> HTMLResponse:
    """Returns HTML/JS/CSS of the view block of the ad. Should be called by JS-library on the client website."""

    if client_id <= 0:
        return HTMLResponse("""
            <html>
                <head>
                    <style></style>
                </head>
                <body>
                    Florgon Ads improperly configured!
                </body>
            </html>
        """)
        
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
