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
