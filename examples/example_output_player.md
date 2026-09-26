# Exemplo — Agente 1 (Criador de Jogadores)

**Pedido do usuário:**
> "Quero um armador de 6'5 com enterradas do Vince Carter, controle de bola do Kyrie Irving e mid-range do Kobe, pra MyCAREER."

**Pergunta do agente antes de montar:**
> Perfeito — já sei que é pra MyCAREER. Só confirmando a plataforma, isso muda a disponibilidade de algumas animações: você joga em current-gen (PS5/Series X) ou last-gen (PS4/Xbox One)?

**Resposta final (formato ilustrativo — os valores reais dependem do modelo em execução):**

```
JOGADOR
Nome: (definido pelo usuário)
Posição: Armador (PG)
Altura: 6'5"
Peso: 195 lbs
Envergadura: 6'7"
Mão dominante: Destro
Número: 11

ATRIBUTOS
Finalização: alta (perto do máximo em finalização acima do aro)
Arremesso: mid-range muito alto, 3PT médio-alto
Playmaking: ball handle e passe muito altos
Defesa/Rebote: moderada, priorizando agilidade
Físico: velocidade e aceleração altas, força moderada

ANIMAÇÕES
Dribble Style: estilo de handle avançado (referência: Kyrie Irving)
Signature Size-Up: combo de hesitation + crossover de alto nível
Layup/Dunk: pacote de finalização aérea (referência: Vince Carter)
Jump Shot: base compacta, release rápido, alta consistência em mid-range
  (referência: Kobe Bryant)

BADGES
Essenciais: Handles for Days, Aerial Wizard, Slithery Finisher
Complementares: Difficult Shots, Mismatch Expert

TENDÊNCIAS
(não aplicável — MyCAREER não expõe configuração direta de tendências
como MyNBA/MyLEAGUE)

CONCEITO
Base física e de playmaking pensada pra sustentar handle de elite,
com pacote de finalização aérea puxando pro estilo Vince Carter e
o jump shot ajustado pra imitar a mecânica de mid-range do Kobe.

LIMITAÇÕES DO NBA 2K26
Não existe uma animação "idêntica" ao Vince Carter ou ao Kobe —
o pacote de finalização e o jump shot escolhidos são as opções mais
próximas disponíveis no editor pro modo MyCAREER.
```

---

Este exemplo é estático (não chama a API) — serve só pra mostrar o formato de saída esperado do agente sem precisar de uma `ANTHROPIC_API_KEY` configurada.
