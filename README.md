# AI Classifying Agent

A small LangChain agent that classifies a message as a **greeting** or a **question**
and replies accordingly.

## Setup

Requires Python 3.10+.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```
ANTHROPIC_API_KEY=your-key-here
```

## Run

```bash
python main.py
```

## Test

```bash
pytest
```
