"""
Base chains module for the LLM agent system.

This file defines the chain registry and configuration for the agent's processing
chains. Chains are sequences of operations that process inputs, interact with LLMs,
and produce structured outputs, allowing for complex reasoning patterns.

Common use cases:
- Creating multi-step reasoning processes
- Structuring conversation flows
- Implementing custom processing logic
- Chaining together multiple LLM calls
- Managing complex interaction patterns

The chain system is based on LangChain's chain architecture and can be customized
for specific use cases with different processing steps and behaviors.
"""

from typing import Any
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_base_chain(llm: BaseLanguageModel) -> Any:
    """Get the base processing chain

    Args:
        llm: The language model to use

    Returns:
        Chain: The processing chain
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant that can use tools when needed.",
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    return prompt | llm
