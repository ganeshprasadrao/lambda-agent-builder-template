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
