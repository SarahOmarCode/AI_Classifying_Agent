"""Settings for the app, read from environment variables (or a .env file)."""

import os

from dotenv import load_dotenv

# Read key=value pairs from a .env file in the project folder (if there is one)
# and put them into the environment, so os.getenv can see them.
load_dotenv()

# Which Claude model to use. You can override it in .env with MODEL_NAME=...
MODEL_NAME = os.getenv("MODEL_NAME", "claude-sonnet-5")

# Your secret API key from https://console.anthropic.com
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# 0 = predictable answers, higher = more creative answers.
TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))
