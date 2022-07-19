from fastapi.responses import HTMLResponse
from app.database.models.ad import Ad


def ads_view_block_html_renderer(ad: Ad) -> HTMLResponse:
    if not ad:
        html_frame = _get_html_frame(
            ad_link="#",
            ad_type="text",
            ad_data="Sorry, no ad was found for you! =("
        )
    else:
        html_frame = _get_html_frame(
            ad_link=f"https://ads.florgon.space/c?aid={ad.id}",
            ad_type=ad.type,
            ad_data=ad.data
        )

    return HTMLResponse(content=html_frame)

def _get_html_frame(ad_link: str, ad_type: str, ad_data: str):
    
    if ad_type == "text":
        ad_body = f"<span>{ad_data}<span/>"
    elif ad_type == "image":
        ad_body = "Unsupported ad type."
    elif ad_type == "video":
        ad_body = "Unsupported ad type."
    else:
        ad_body = "Unknown ad type."

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
                <a href='{ad_link}' target='_blank' rel='opener'>{ad_body}</a>
            </body>
        </html>
    """.format(css=css, ad_link=ad_link, ad_body=ad_body)
    return html