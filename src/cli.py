import sys

from .agents import run_agent
from .client import get_client

AGENT_LABELS = {
    "1": ("player", "Criador de Jogadores"),
    "2": ("team", "Criador de Times"),
}


def choose_agent() -> str:
    print("Qual agente você quer usar?")
    print("  1 - Criador de Jogadores")
    print("  2 - Criador de Times")
    choice = input("> ").strip()
    if choice not in AGENT_LABELS:
        print("Opção inválida. Encerrando.")
        sys.exit(1)
    key, label = AGENT_LABELS[choice]
    print(f"\nConversando com: {label}")
    return key


def main() -> None:
    client = get_client()
    agent_key = choose_agent()
    print("Digite 'sair' para encerrar a conversa.\n")

    history: list[dict] = []
    while True:
        try:
            user_input = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando.")
            break

        if not user_input:
            continue
        if user_input.lower() in {"sair", "exit", "quit"}:
            break

        history.append({"role": "user", "content": user_input})
        reply = run_agent(client, agent_key, history)
        print(f"\nAgente: {reply}\n")
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
