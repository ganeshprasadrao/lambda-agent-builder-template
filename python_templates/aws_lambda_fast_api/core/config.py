"""
Application configuration settings using Pydantic.

This file defines the application settings using Pydantic's BaseSettings,
which allows for type-safe configuration management with environment
variables and .env file support. Settings are cached using lru_cache
for performance optimization.

Common use cases:
- Environment-specific configuration
- API metadata configuration
- Database connection settings
- AWS region configuration
- Logging level configuration

To override settings, create a .env file or set environment variables.
"""

from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""

    # API Configuration
    API_TITLE: str = "FastAPI Lambda Service"
    API_DESCRIPTION: str = "A FastAPI application deployed on AWS Lambda"
    API_VERSION: str = "1.0.0"

    # Database Configuration (example)
    DATABASE_URL: Optional[str] = None

    # AWS Configuration
    AWS_REGION: str = "us-east-1"

    # Logging Configuration
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
