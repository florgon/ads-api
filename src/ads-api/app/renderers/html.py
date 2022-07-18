from fastapi.responses import HTMLResponse
from app.database.models.ad import Ad


def ads_view_block_html_renderer(ad: Ad) -> HTMLResponse:
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