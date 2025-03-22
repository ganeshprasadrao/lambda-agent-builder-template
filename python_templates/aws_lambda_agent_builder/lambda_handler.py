"""
AWS Lambda handler for the LLM-based Agent application.

This file serves as the entry point for AWS Lambda, using Mangum to connect the
FastAPI application with AWS Lambda. It translates AWS Lambda events to ASGI-compatible
requests that the FastAPI application can handle.

Common use cases:
- AWS Lambda deployment of FastAPI applications
- Serverless AI agent deployment
- API Gateway integration
- Event-triggered AI agent processing
- Cost-effective scalable AI deployments

This handler exposes the FastAPI application to AWS Lambda, enabling serverless
execution of the LLM agent without running a dedicated server.
"""

from mangum import Mangum
from main import app

# Create Lambda handler
lambda_handler = Mangum(app, lifespan="off")


# Lambda handler function
def lambda_handler(event, context):
    """AWS Lambda handler function

    Args:
        event: AWS Lambda event
        context: AWS Lambda context

    Returns:
        dict: API Gateway response
    """
    return lambda_handler(event, context)
