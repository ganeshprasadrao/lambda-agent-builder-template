"""
API router configuration for version 1.

This file sets up the main API router for version 1 of the API, importing and
including all endpoint routers. It establishes the routing structure and prefix
for all v1 endpoints.

Common use cases:
- API versioning
- Organizing routes by functionality
- Centralized API route definition
- Simplified API structure maintenance

This is a key file for API structure as it imports all endpoint routers and
combines them under the v1 prefix, allowing for clean versioning of the API.
"""

from fastapi import APIRouter
from api.v1.endpoints import health

# Main v1 API router
api_router = APIRouter()

# Include all endpoint routers with appropriate tags and prefixes
api_router.include_router(health.router, tags=["health"])
