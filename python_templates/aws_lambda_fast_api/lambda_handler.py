"""
AWS Lambda handler for the FastAPI application.

This file connects the FastAPI application with AWS Lambda using Mangum.
It creates a handler that translates between AWS Lambda events and the ASGI
interface expected by FastAPI. This is a standardized way to deploy FastAPI
applications on AWS Lambda.

Common use cases:
- Serverless deployment of FastAPI applications
- API Gateway integration
- EventBridge triggered APIs
- Scheduled tasks via EventBridge rules

Note: This file should not be modified unless you need custom AWS Lambda event handling.
"""

from mangum import Mangum
from main import app

# Create handler for AWS Lambda
handler = Mangum(app)


# Lambda handler function
def lambda_handler(event, context):
    """AWS Lambda handler function

    Args:
        event: AWS Lambda event
        context: AWS Lambda context

    Returns:
        dict: API Gateway response
    """
    return handler(event, context)
