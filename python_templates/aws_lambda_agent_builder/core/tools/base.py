"""
Base tools module for the LLM agent system.

This file defines the tool registry and loading mechanism for the agent's tools.
Tools extend the agent's capabilities by allowing it to perform specific actions
such as searching data, accessing APIs, or processing information.

Common use cases:
- Registering custom tools for the agent
- Enabling function calling capabilities
- Integrating external APIs and services
- Performing specialized tasks like data retrieval or computation
- Building agents with specific domain capabilities

The tool system follows LangChain's tool structure and can be easily extended
with custom tools specific to your application's needs.
"""

from typing import List, Dict, Any
from langchain_core.tools import BaseTool, tool


@tool
def example_tool(input_str: str) -> str:
    """A simple example tool that echoes the input

    Args:
        input_str: The input string to echo

    Returns:
        str: The echoed input
    """
    return f"Echo: {input_str}"


def get_tools() -> List[BaseTool]:
    """Get all available tools

    Returns:
        List[BaseTool]: List of available tools
    """
    # Add your custom tools here
    tools = [
        example_tool,
    ]

    return tools
