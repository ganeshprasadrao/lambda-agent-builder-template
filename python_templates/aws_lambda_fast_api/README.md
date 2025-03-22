# AWS Lambda FastAPI Template

A lightweight template for building FastAPI applications deployed on AWS Lambda.

## Features

- High-performance API endpoints with FastAPI
- AWS Lambda deployment using Zappa
- Environment management and security best practices
- Comprehensive logging with Loguru
- Serverless architecture for scalability
- Local development environment

## Getting Started

### Prerequisites

- Python 3.12+
- AWS CLI configured with appropriate credentials
- Virtual environment tool (e.g., venv, conda)

### Installation

1. Clone this repository

   ```bash
   git clone https://github.com/ganeshprasadrao/templates-hq.git
   cd templates-hq/python_templates/aws_lambda_fast_api
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -e .
   ```

4. Create a `.env` file with your configuration
   ```
   LOG_LEVEL=INFO
   API_TITLE="My FastAPI Service"
   API_DESCRIPTION="Custom API description"
   API_VERSION="1.0.0"
   ```

### Local Development

Run the application locally:

```bash
python main.py
```

The API will be available at `http://localhost:8000`.

### API Documentation

Once the application is running, you can access the Swagger UI documentation at:

- Local: `http://localhost:8000/docs`
- After deployment: `https://[your-api-gateway-url]/prod/docs`

## Deployment

### Configure Zappa

Update the `zappa_settings.json` file with your configuration:

```json
{
  "prod": {
    "app_function": "lambda_handler.handler",
    "profile_name": "your-aws-profile",
    "project_name": "your-project-name",
    "runtime": "python3.12",
    "s3_bucket": "your-deployment-bucket"
  }
}
```

### Deploy to AWS Lambda

```bash
zappa deploy prod
```

### Update Existing Deployment

```bash
zappa update prod
```

## Project Structure

```
.
├── core/                  # Core application components
│   ├── config.py         # Application configuration
│   └── utils/            # Utility functions
│       ├── asgi_to_wsgi.py  # ASGI to WSGI converter
│       └── logger.py     # Logging configuration
├── lambda_handler.py     # AWS Lambda handler
├── main.py               # FastAPI application
├── pyproject.toml        # Project dependencies
├── README.md             # Project documentation
└── zappa_settings.json   # Zappa deployment configuration
```

## Customization

### Adding Routes

Add new routes in `main.py` or create separate route modules under a `routers` directory.

### Database Integration

For database integration, consider adding an async database client in the `core` directory and connecting it in `main.py`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
