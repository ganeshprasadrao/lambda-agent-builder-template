"""
Main API configuration file.

This file configures the main API router that combines all versioned API routers
(v1, v2, etc.) and applies global configurations like prefixes and middleware.
It acts as the central API router registry for the application.

Common use cases:
- Centralized API versioning
- Global API configuration
- API prefix management
- Integration point for all API versions
- Application of cross-cutting API concerns like CORS, rate limiting, etc.

The API structure allows for multiple versions to coexist, making it easy to
evolve the API while maintaining backward compatibility.
"""

from fastapi import APIRouter
from api.v1.api import api_router as api_v1_router

# Main API router that combines all versioned routers
api_router = APIRouter()

# Include versioned API routers with appropriate prefixes
api_router.include_router(api_v1_router, prefix="/v1")
