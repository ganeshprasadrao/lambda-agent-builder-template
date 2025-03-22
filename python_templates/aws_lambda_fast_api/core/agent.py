from typing import Dict, List, Any, Optional
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from core.tools.base import get_tools
from core.chains.base import get_base_chain
from core.config import get_settings
from core.utils.logger import get_logger
from pydantic import BaseModel


logger = get_logger(__name__)
settings = get_settings()


class AgentError(Exception):
    """Base exception for agent-related errors"""

    pass


class AgentConfig(BaseModel):
    """Configuration model for Agent initialization"""

    model_name: str = settings.MODEL_NAME
    temperature: float = settings.TEMPERATURE
    streaming: bool = settings.STREAMING


class Agent:
    """Base Agent class that can be extended for specific use cases"""

    def __init__(self, config: Optional[AgentConfig] = None):
        """Initialize the agent with specific configuration

        Args:
            config: Optional configuration override
        """
        self.config = config or AgentConfig()
        self._setup_agent()
        logger.info("Agent initialized with model: {}", self.config.model_name)

    def _setup_agent(self) -> None:
        """Set up the agent's components"""
        try:
            self.llm = ChatOpenAI(
                model=self.config.model_name,
                temperature=self.config.temperature,
                streaming=self.config.streaming,
            )
            self.tools = get_tools()
            self.llm_with_tools = self.llm.bind_tools(self.tools)
            self.chain = get_base_chain(self.llm_with_tools)
        except Exception as e:
            logger.error("Failed to setup agent: {}", str(e))
            raise AgentError(f"Agent setup failed: {str(e)}")

    def invoke(self, query: str, context: Dict[str, Any] = None) -> List[AIMessage]:
        """Process a query through the agent

        Args:
            query: The user's query
            context: Optional context dictionary

        Returns:
            List[AIMessage]: The conversation messages

        Raises:
            AgentError: If processing fails
        """
        try:
            logger.debug("Processing query: {}", query)

            # Create initial messages
            messages = [
                SystemMessage(content=self._get_system_prompt(context)),
                HumanMessage(content=query),
            ]

            # Process through chain
            response = self.chain.invoke(messages)

            logger.debug("Query processed successfully")
            return messages + [response]

        except Exception as e:
            logger.error("Query processing failed: {}", str(e))
            raise AgentError(f"Failed to process query: {str(e)}")

    def _get_system_prompt(self, context: Dict[str, Any] = None) -> str:
        """Get the system prompt for the agent

        Args:
            context: Optional context to customize the prompt

        Returns:
            str: The system prompt
        """
        base_prompt = """You are a helpful AI assistant. Your task is to:
1. Understand and analyze user requests
2. Use available tools when necessary
3. Provide clear and concise responses
4. Handle errors gracefully
5. Maintain context throughout the conversation"""

        if context and context.get("custom_instructions"):
            base_prompt += (
                f"\n\nAdditional Instructions:\n{context['custom_instructions']}"
            )

        return base_prompt


def create_agent(**kwargs) -> Agent:
    """Factory function to create an agent instance

    Args:
        **kwargs: Configuration overrides

    Returns:
        Agent: Configured agent instance
    """
    config = AgentConfig(**kwargs)
    return Agent(config)
