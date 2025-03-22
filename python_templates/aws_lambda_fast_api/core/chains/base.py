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
