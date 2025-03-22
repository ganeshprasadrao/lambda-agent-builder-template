import logging
import sys
from loguru import logger
from core.config import get_settings

# Get settings
settings = get_settings()

# Configure loguru
logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            "level": settings.LOG_LEVEL,
        }
    ]
)


class InterceptHandler(logging.Handler):
    """Intercept standard logging messages towards loguru"""

    def emit(self, record):
        # Get corresponding loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where the logged message originated
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging():
    """Set up logging configuration"""
    # Intercept standard logging to loguru
    logging.basicConfig(handlers=[InterceptHandler()], level=0)

    # Disable uvicorn access logs in INFO level
    for logger_name in logging.root.manager.loggerDict:
        if logger_name.startswith("uvicorn."):
            logging.getLogger(logger_name).handlers = [InterceptHandler()]


def get_logger(name):
    """Get a logger for the specified name"""
    setup_logging()
    return logger.bind(name=name)
