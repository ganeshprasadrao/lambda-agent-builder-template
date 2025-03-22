"""
API health check endpoint.

This file defines a simple health check endpoint that returns a 200 OK response
when the API is functioning properly. It serves as a minimal example of a FastAPI
router implementation and can be used for monitoring and load balancer health checks.

Common use cases:
- Kubernetes liveness and readiness probes
- AWS ELB/ALB health checks
- Service monitoring
- Simple endpoint for testing API availability

The health endpoint follows RESTful API standards and can be extended to include
more detailed health information about dependent services, database connections, etc.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", status_code=200)
async def health_check():
    """
    Health check endpoint.

    Returns:
        dict: A simple message indicating the API is healthy
    """
    return {"status": "healthy", "message": "API is up and running"}
