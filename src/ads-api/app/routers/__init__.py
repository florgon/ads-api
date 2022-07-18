"""
    Ads server API routers.
    (FastAPI routers)
"""

from fastapi import FastAPI

from app.config import get_settings

from . import (
    utils,
    ads,
)


def register_routers(app: FastAPI) -> None:
    """
    Registers FastAPI routers.
    """
    # Routers.
    for router in [utils.router, ads.router]:
        app.include_router(router, prefix=get_settings().proxy_url_prefix)
