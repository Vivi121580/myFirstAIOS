from __future__ import annotations

from pathlib import Path

from .agent import PersonalAgent
from .semantic_rag import SemanticRAG


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    rag = SemanticRAG(project_root)
    agent = PersonalAgent()
    agent.memory.add("startup", "Application initialized")

    print("myFirstAIOS started.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You> ").strip()
        if user_input.lower() in {"exit", "quit", "q"}:
            print("Goodbye.")
            break

        response = agent.respond(user_input)
        response += "\n\nRelevant knowledge:\n" + rag.answer(user_input)
        print(f"\nAssistant> {response}\n")


if __name__ == "__main__":
    main()
