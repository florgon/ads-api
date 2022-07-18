"""
    Standartized API error codes container.
"""

from enum import Enum


class ApiErrorCode(Enum):
    """API Standartized error codes."""

    API_UNKNOWN_ERROR = 0, 500
    API_INVALID_REQUEST = 1, 400
    API_INTERNAL_SERVER_ERROR = 2, 500
    API_EXTERNAL_SERVER_ERROR = 3, 500
    API_METHOD_NOT_FOUND = 4, 404
    API_NOT_IMPLEMENTED = 5, 400

    AUTH_INVALID_TOKEN = 6, 400
    AUTH_EXPIRED_TOKEN = 7, 400
    AUTH_REQUIRED = 8, 401
    AUTH_INSUFFICIENT_PERMISSSIONS = 9, 403

    USER_DEACTIVATED = 8, 403


class ApiErrorException(Exception):
    def __init__(
        self, api_code: ApiErrorCode, message: str = "", data: dict | None = None
    ):
        self.api_code = api_code
        self.message = message
        self.data = data
