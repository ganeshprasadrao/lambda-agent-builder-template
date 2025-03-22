"""
HTTP error handling module.

This file defines the custom HTTP error handling classes and utility functions that can
be used throughout the FastAPI application to standardize error responses.

The module provides:
- A base HTTPError class that extends FastAPI's HTTPException
- Factory functions for creating common HTTP errors
- Consistent error response structure with status code, message, and details

Common use cases:
- Standardized API error responses
- Consistent error handling across the application
- Custom error types with specific status codes
- Detailed error reporting with structured details

This error system integrates with FastAPI's exception handling to ensure all errors
follow the same structure in API responses.
"""

from typing import Any, Dict, Optional
from fastapi import HTTPException
from starlette import status


class HTTPError(HTTPException):
    """Base class for HTTP errors with standard structure."""

    def __init__(
        self,
        status_code: int,
        message: str,
        details: Optional[Dict[str, Any]] = None,
    ):
        self.status_code = status_code
        self.message = message
        self.details = details
        super().__init__(
            status_code=status_code, detail={"message": message, "details": details}
        )


def http_error_400(message: str, details: Optional[Dict[str, Any]] = None) -> HTTPError:
    """Return a 400 Bad Request error."""
    return HTTPError(
        status_code=status.HTTP_400_BAD_REQUEST, message=message, details=details
    )


def http_error_401(message: str, details: Optional[Dict[str, Any]] = None) -> HTTPError:
    """Return a 401 Unauthorized error."""
    return HTTPError(
        status_code=status.HTTP_401_UNAUTHORIZED, message=message, details=details
    )


def http_error_403(message: str, details: Optional[Dict[str, Any]] = None) -> HTTPError:
    """Return a 403 Forbidden error."""
    return HTTPError(
        status_code=status.HTTP_403_FORBIDDEN, message=message, details=details
    )


def http_error_404(message: str, details: Optional[Dict[str, Any]] = None) -> HTTPError:
    """Return a 404 Not Found error."""
    return HTTPError(
        status_code=status.HTTP_404_NOT_FOUND, message=message, details=details
    )


def http_error_500(message: str, details: Optional[Dict[str, Any]] = None) -> HTTPError:
    """Return a 500 Internal Server Error."""
    return HTTPError(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message=message,
        details=details,
    )
