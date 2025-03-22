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
