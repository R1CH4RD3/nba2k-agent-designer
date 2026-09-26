import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


def get_client() -> Anthropic:
    # falha cedo e com uma mensagem que dá pra entender, em vez de deixar
    # o SDK estourar um erro genérico lá na frente
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY não encontrada. Copia o .env.example pra .env "
            "e cola sua chave lá dentro."
        )
    return Anthropic(api_key=api_key)
