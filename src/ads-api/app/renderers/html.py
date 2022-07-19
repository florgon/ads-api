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
    html = """
        <html>
            <head>
                <style>
                    {css}
                </style>
            </head>
            <body>
                <a href='{ad_link}'>{ad_text}</a>
            </body>
        </html>
    """
    html = html.format(css=css, ad_link=ad_link, ad_text=ad_text)
    return HTMLResponse(content=html)