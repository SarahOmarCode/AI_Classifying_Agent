"""The agent: classify the message first, then send it to the matching responder."""

from app.classifier import classify
from app.llm import get_llm
from app.responders import build_greeting_responder, build_question_responder


class ClassifyingAgent:
    def __init__(self, llm=None):
        # Passing an llm in is optional. Tests use it to pass a fake one,
        # so they don't need an API key or internet.
        self.llm = llm or get_llm()

        # One responder chain per category. Adding a new category later means
        # adding a label in classifier.py, a prompt, and an entry here.
        self.responders = {
            "greeting": build_greeting_responder(self.llm),
            "question": build_question_responder(self.llm),
        }

    def run(self, query):
        """Handle one user message and return the label and the reply."""
        label = classify(query, self.llm)
        response = self.responders[label].invoke({"query": query})
        return {"label": label, "response": response}
