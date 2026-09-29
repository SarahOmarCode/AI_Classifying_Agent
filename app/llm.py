"""Creates the chat model (the LLM) that the rest of the app talks to."""

from langchain_anthropic import ChatAnthropic

from app import config


def get_llm():
    """Return a LangChain chat model connected to Claude."""
    if not config.ANTHROPIC_API_KEY:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. Add it to a .env file in the project folder."
        )

    return ChatAnthropic(
        model=config.MODEL_NAME,
        api_key=config.ANTHROPIC_API_KEY,
        temperature=config.TEMPERATURE,
    )
