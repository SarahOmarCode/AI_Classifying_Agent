"""Generates the reply, using a different prompt for each category."""

from langchain_core.output_parsers import StrOutputParser

from app.prompts import GREETING_PROMPT, QUESTION_PROMPT


def build_greeting_responder(llm):
    """Chain that answers greetings. StrOutputParser turns the reply into a plain string."""
    return GREETING_PROMPT | llm | StrOutputParser()


def build_question_responder(llm):
    """Chain that answers questions."""
    return QUESTION_PROMPT | llm | StrOutputParser()
