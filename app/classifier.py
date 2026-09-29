"""Decides whether a user's message is a greeting or a question."""

from typing import Literal

from pydantic import BaseModel, Field

from app.prompts import CLASSIFIER_PROMPT


class Classification(BaseModel):
    """The shape of the answer we want back from the LLM.

    Literal[...] means the LLM is only allowed to return one of these two words.
    """

    label: Literal["greeting", "question"] = Field(
        description="The category of the user's message."
    )


def build_classifier(llm):
    """Build the classification chain: prompt -> LLM -> Classification object.

    The | symbol ("pipe") connects steps: the output of the left side becomes
    the input of the right side. This is called LCEL (LangChain Expression Language).

    with_structured_output makes the LLM reply with a Classification object
    instead of free text, so we never have to parse its words ourselves.
    """
    return CLASSIFIER_PROMPT | llm.with_structured_output(Classification)


def classify(query, llm):
    """Return "greeting" or "question" for the given user message."""
    result = build_classifier(llm).invoke({"query": query})
    return result.label
