from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, List
from core.config import get_settings
from core.utils.logger import get_logger
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize logger
logger = get_logger(__name__)

# Get settings
settings = get_settings()

# Initialize FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
)


class Item(BaseModel):
    """Sample data model for API"""

    id: int
    name: str
    description: str = None


@app.get("/items/", response_model=List[Item])
async def get_items():
    """Get a list of sample items

    Returns:
        List[Item]: A list of sample items
    """
    logger.info("Fetching items")
    return [
        Item(id=1, name="Item 1", description="Description for Item 1"),
        Item(id=2, name="Item 2", description="Description for Item 2"),
    ]


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID

    Args:
        item_id: The ID of the item to retrieve

    Returns:
        Item: The requested item

    Raises:
        HTTPException: If the item is not found
    """
    logger.info(f"Fetching item {item_id}")

    # Sample data - in a real app, this would come from a database
    items = {
        1: Item(id=1, name="Item 1", description="Description for Item 1"),
        2: Item(id=2, name="Item 2", description="Description for Item 2"),
    }

    if item_id not in items:
        logger.warning(f"Item {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")

    return items[item_id]


@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    """Create a new item

    Args:
        item: The item to create

    Returns:
        Item: The created item
    """
    logger.info(f"Creating item: {item.name}")
    # In a real app, this would save to a database
    return item


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": settings.API_VERSION}


if __name__ == "__main__":
    import uvicorn
    from loguru import logger
    import logging

    # Configure uvicorn logging to use loguru
    class InterceptHandler(logging.Handler):
        def emit(self, record):
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = record.levelno

            frame, depth = logging.currentframe(), 2
            while frame.f_code.co_filename == logging.__file__:
                frame = frame.f_back
                depth += 1

            logger.opt(depth=depth, exception=record.exc_info).log(
                level, record.getMessage()
            )

    # Update uvicorn logging config
    logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.error").handlers = [InterceptHandler()]

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
