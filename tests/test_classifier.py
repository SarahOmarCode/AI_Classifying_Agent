"""Tests that run without an API key, using a fake LLM.

Run them with: pytest
"""

from langchain_core.language_models.fake_chat_models import FakeListChatModel
from langchain_core.runnables import RunnableLambda

from app.agent import ClassifyingAgent
from app.classifier import Classification, classify


class FakeLLM(FakeListChatModel):
    """A pretend LLM.

    - For classification it returns a fixed label (no real AI involved).
    - For replies it returns the canned strings in `responses`, in order.
    """

    label: str = "question"

    def with_structured_output(self, schema, **kwargs):
        return RunnableLambda(lambda _prompt: Classification(label=self.label))


def test_classify_greeting():
    llm = FakeLLM(responses=[], label="greeting")
    assert classify("Hello there!", llm) == "greeting"


def test_classify_question():
    llm = FakeLLM(responses=[], label="question")
    assert classify("What is LangChain?", llm) == "question"


def test_agent_routes_greeting_to_greeting_responder():
    llm = FakeLLM(responses=["Hi! How can I help?"], label="greeting")
    result = ClassifyingAgent(llm=llm).run("Hello")
    assert result == {"label": "greeting", "response": "Hi! How can I help?"}


def test_agent_routes_question_to_question_responder():
    llm = FakeLLM(responses=["LangChain is a framework for LLM apps."], label="question")
    result = ClassifyingAgent(llm=llm).run("What is LangChain?")
    assert result["label"] == "question"
    assert result["response"] == "LangChain is a framework for LLM apps."
