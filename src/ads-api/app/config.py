"""
    Config environment variables reader.
"""

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    """Base settings."""

    database_url: PostgresDsn

    sso_api_url: str
    sso_api_method: str

    proxy_url_prefix: str
    proxy_url_host: str

    fastapi_debug: bool = False
    cors_enabled: bool = True

_settings = Settings()


def get_settings():
    return _settings
