from flask import *


app = Flask(__name__)


def _get_html_frame(ad_link: str, ad_type: str, ad_data: str):

    if ad_type == "text":
        ad_body = f"<span>{ad_data}<span/>"
    elif ad_type == "image":
        ad_body = f"<img src='{ad_data}'>Browser not compatible with this ad.</img>"
    elif ad_type == "video":
        ad_body = f"<video src='{ad_data}'>Browser not compatible with this ad.</video>"
    else:
        ad_body = "Unknown ad type."

    css = """
        html, body, img { 
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
    """.format(
        css=css, ad_link=ad_link, ad_body=ad_body
    )
    return html


@app.route("/get_ads_text")
def get_ads_text():
    return _get_html_frame("http://0nera.ru", "text", "Fuck")


@app.route("/get_ads_img")
def get_ads_img():
    return _get_html_frame("http://0nera.ru", "image", "https://wiki.osdev.org/skins/common/images/osdev.png")


@app.route("/get_ads_video")
def get_ads_video():
    return _get_html_frame("http://0nera.ru", "video", "Fuck")


@app.route("/")
def test_me_full():
    return """
<iframe src="/get_ads_text"></iframe>
<iframe src="/get_ads_img"></iframe>
<iframe src="/get_ads_video"></iframe>

"""




if __name__ == '__main__':
    app.run(debug = True, port = 5555)