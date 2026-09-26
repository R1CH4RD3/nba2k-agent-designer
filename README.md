# nba2k-agent-designer

Um projeto pequeno que nasceu de uma dúvida boba: dá pra transformar "quero um armador com o handle do Kyrie e a finalização do Vince Carter" em uma build de verdade, pronta pra copiar no editor do NBA 2K26, sem o agente inventar recurso que o jogo não tem?

A resposta virou dois agentes conversando com a API da Anthropic, cada um especializado numa parte do problema.

## O que isso faz

- **Agente Criador de Jogadores** — recebe uma descrição (mistura de jogadores reais, ideia original, recriação histórica) e devolve uma ficha completa: atributos, animações, badges e tendências, sempre checando antes se é pra MyCAREER ou MyNBA (isso muda bastante o que fica disponível).
- **Agente Criador de Times** — parte de uma ideia solta tipo "franquia futurista de Seattle" e monta identidade, história, uniformes, logos (com prompt de geração de imagem pronto pra usar) e conceito de quadra.

O ponto chato dos dois, e o motivo de eu ter me dado ao trabalho de escrever isso: eles são instruídos a nunca fingir que um recurso existe. Quando o pedido não tem equivalente exato no jogo, a resposta precisa dizer isso e oferecer a alternativa mais próxima. Parece um detalhe pequeno, mas é o que separa um agente útil de um que só parece saber do assunto.

## Por que separar em dois agentes

Dava pra fazer um prompt gigante fazendo as duas coisas, mas achei melhor não. Jogador e franquia têm formatos de saída, restrições e vocabulário bem diferentes, e misturar tudo num prompt só ia deixar o raciocínio mais raso nas duas pontas. Separado, cada um fica mais fácil de testar e ajustar sem quebrar o outro — a mesma lógica de manter funções pequenas e com uma responsabilidade só.

## Como rodar

```bash
git clone https://github.com/R1CH4RD3/nba2k-agent-designer
cd nba2k-agent-designer
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # cola sua ANTHROPIC_API_KEY ali dentro
python main.py
```

O script pergunta qual dos dois agentes você quer usar e abre um chat direto no terminal. `sair` encerra.

## Estrutura

```
agents/          system prompts dos dois agentes — é aqui que mora a parte "inteligente"
src/client.py    inicializa o cliente da Anthropic
src/agents.py    lê o prompt certo e chama o modelo
src/cli.py       loop de chat no terminal
examples/        um exemplo de saída real, pra quem quiser ver sem precisar de chave de API
```

## O que ainda falta

Hoje é só uma CLI simples. O próximo passo óbvio seria validar as animações e badges citadas contra uma lista real de conteúdo do jogo (o modelo pode, raramente, citar algo que não existe mais numa versão específica), e talvez subir isso como uma API pequena com FastAPI em vez de só terminal.

## Stack

Python, SDK oficial da Anthropic, dotenv. Nada além disso, de propósito.
