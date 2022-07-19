"""
    Florgon Ads API server entry point.
    FastAPI server.
"""

from fastapi import FastAPI

# Settings.
from .config import get_settings

# ORM constructor.
from . import database

# Setters for custom layers.
from .middlewares import add_middlewares

# from .event_handlers import add_event_handlers
from .routers import register_routers
from .exception_handlers import register_handlers


def _construct_app() -> FastAPI:
    """
    Returns FastAPI application ready to run.
    Creates base FastAPI instance with registering all required stuff on it.
    """

    settings = get_settings()
    app_instance = FastAPI(
        # FastAPI debug.
        debug=settings.fastapi_debug,
        # Custom settings.
        # By default, modified by setters (below), or empty if not used.
        routes=None,
        middleware=None,
        exception_handlers=None,
        dependencies=None,
        responses=None,
        callbacks=None,
        on_shutdown=None,
        on_startup=None,
        # Documentation settings.
        # Notice that documentation is disabled by default and recommended to be disabled.
        # title=settings.fastapi_title,
        # description=settings.fastapi_description,
        # Disable any documentation.
        # openapi_url="/openapi.json" if settings.fastapi_documentation_enabled else None,
        # docs_url="/docs" if settings.fastapi_documentation_enabled else None,
        # redoc_url="/redoc" if settings.fastapi_documentation_enabled else None,
    )

    # Initialising database connection and all ORM stuff.
    database.core.create_all()

    # Register all internal stuff as routers/handlers/middlewares etc.
    # add_event_handlers(app_instance)
    add_middlewares(app_instance)
    register_handlers(app_instance)
    register_routers(app_instance)

    return app_instance


# Root application for uvicorn runner or whatever else.
# (Docker compose is running with app.app:app, means that this application instance
# will be served by uvicorn, and will be constructed at import).
app = _construct_app()
