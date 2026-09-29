"""Run the agent in the terminal: python main.py"""

from app.agent import ClassifyingAgent


def main():
    agent = ClassifyingAgent()
    print("Classifying agent ready. Type a message (or 'quit' to exit).")

    while True:
        query = input("\nYou: ").strip()
        if not query:
            continue
        if query.lower() in ("quit", "exit"):
            break

        result = agent.run(query)
        print(f"[classified as: {result['label']}]")
        print(f"Agent: {result['response']}")


if __name__ == "__main__":
    main()
