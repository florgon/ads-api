from fastapi.responses import HTMLResponse
from app.database.models.ad import Ad


def ads_view_block_html_renderer(ad: Ad) -> HTMLResponse:
    if not ad:
        ad_text = "Sorry, no ad was found for you! =("
        ad_link = "#"
    else:
        ad_text = ad.text
        ad_link = f"https://ads.florgon.space/c?aid={ad.id}"

    css = """
        html, body { 
            margin: 0; 
            padding: 0; 
            width: 100%; 
            height: 100%; 
        }
        a { 
            display: block; 
            width: 100%; 
            height: 100%; 
            text-decoration: none; 
            color: black;
        }
    """
    if ad.type == "text":
        html_body = f"<a href='{ad_link}' target='_blank' rel='opener'>{ad_text}</a>"
    else:
        html_body = "unknown ad type."
    html = """
        <html>
            <head>
                <style>
                    {css}
                </style>
            </head>
            <body>
                {html_body}
            </body>
        </html>
    """
    html = html.format(css=css, html_body=html_body)
    return HTMLResponse(content=html)