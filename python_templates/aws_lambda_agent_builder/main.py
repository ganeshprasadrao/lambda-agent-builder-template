from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, List
from core.agent import create_agent, AgentError
from core.config import get_settings
from core.utils.logger import get_logger
import os
from dotenv import load_dotenv
import logging

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

# Create agent instance
agent = create_agent()


class Query(BaseModel):
    """Query model for agent interaction"""

    text: str
    context: Dict[str, Any] = None


class AgentResponse(BaseModel):
    """Response model for agent interaction"""

    messages: List[str]


@app.exception_handler(AgentError)
async def agent_error_handler(request: Request, exc: AgentError):
    """Handle agent-specific errors"""
    logger.error("Agent error: {}", str(exc))
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )


@app.post("/agent/chat", response_model=AgentResponse)
async def chat_with_agent(query: Query) -> AgentResponse:
    """Chat with the AI agent

    Args:
        query: Query containing text and optional context

    Returns:
        AgentResponse: The agent's response messages

    Raises:
        HTTPException: If the request fails
    """
    try:
        logger.info("Received chat request: {}", query.text[:100])

        # Process the query through the agent
        responses = agent.invoke(query.text, query.context)

        # Extract message contents
        messages = [msg.content for msg in responses if hasattr(msg, "content")]

        logger.info("Chat request processed successfully")
        return AgentResponse(messages=messages)

    except AgentError as e:
        # Let the exception handler deal with agent errors
        raise
    except Exception as e:
        logger.error("Unexpected error in chat endpoint: {}", str(e))
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "agent": "initialized", "model": settings.MODEL_NAME}


if __name__ == "__main__":
    import uvicorn
    from loguru import logger

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
    import logging

    logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.error").handlers = [InterceptHandler()]

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
