import pathlib

AGENTS_DIR = pathlib.Path(__file__).resolve().parent.parent / "agents"

AGENT_FILES = {
    "player": "player_agent.md",
    "team": "team_agent.md",
}

DEFAULT_MODEL = "claude-sonnet-4-6"


def load_system_prompt(agent_key: str) -> str:
    if agent_key not in AGENT_FILES:
        raise ValueError(f"Agente desconhecido: '{agent_key}'. Use 'player' ou 'team'.")
    path = AGENTS_DIR / AGENT_FILES[agent_key]
    return path.read_text(encoding="utf-8")


def run_agent(client, agent_key, messages, model=DEFAULT_MODEL, max_tokens=2000):
    # o system prompt inteiro do agente vai junto em toda chamada —
    # simples, mas funciona bem pro tamanho desse projeto
    system_prompt = load_system_prompt(agent_key)
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=messages,
    )
    return "".join(
        block.text for block in response.content if block.type == "text"
    )
