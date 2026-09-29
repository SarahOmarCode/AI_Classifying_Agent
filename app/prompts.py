"""All the prompts (instructions) we send to the LLM, kept in one place.

A ChatPromptTemplate is a list of messages with {placeholders}.
When we run it, LangChain fills in the placeholders with real values.
"""

from langchain_core.prompts import ChatPromptTemplate

# Step 1: decide what kind of message the user sent.
CLASSIFIER_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You classify a user's message into exactly one category:\n"
            "- greeting: hello, hi, good morning, how are you, and similar small talk.\n"
            "- question: anything asking for information, help, or an explanation.\n"
            "If a message contains both a greeting and a question, choose question.",
        ),
        ("human", "{query}"),
    ]
)

# Step 2a: how to answer a greeting.
GREETING_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a friendly assistant. The user greeted you. "
            "Greet them back warmly in one or two short sentences "
            "and offer to help with any question.",
        ),
        ("human", "{query}"),
    ]
)

# Step 2b: how to answer a question.
QUESTION_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer the user's question clearly "
            "and concisely. If you don't know, say so.",
        ),
        ("human", "{query}"),
    ]
)
