from loguru import logger
import sys
from typing import Optional
from core.config import get_settings

settings = get_settings()

# Remove all default handlers
logger.remove()

# Add custom handler with formatting
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level=settings.LOG_LEVEL,
    colorize=True,
)


def get_logger(name: str):
    """Get a contextualized logger instance

    Args:
        name: The name to bind to the logger

    Returns:
        logger: Configured logger instance with context
    """
    return logger.bind(name=name)
