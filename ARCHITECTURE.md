# MIMO-Flow Architecture

O **MIMO-Flow** é um framework modular em Python projetado para orquestração avançada de agentes de codificação autônomos. Este documento detalha a arquitetura do sistema e o fluxo de dados entre os agentes.

## Estrutura de Diretórios

O sistema está dividido de forma modular e escalável:

```text
flow/
├── agents/             # Lógica e comportamento dos agentes
│   ├── base.py         # Classe base para todos os agentes
│   ├── architect.py    # Agente de design (Usa Long-Chain Reasoning)
│   ├── coder.py        # Agente programador
│   └── critic.py       # Agente revisor
├── core/               # Lógica central e orquestração
│   ├── orchestrator.py # Pipeline de execução de agentes
│   └── reasoning.py    # Simulação de planejamento "Long-Chain Reasoning"
├── utils/              # Ferramentas auxiliares
│   └── token_counter.py# Monitoramento de uso de tokens
├── mimo_api/           # Conectividade com a série MiMo
│   └── client.py       # Placeholder do cliente API para os modelos MiMo
└── cli.py              # Interface de linha de comando
```

## Fluxo de Dados (Data Flow)

O fluxo de execução do sistema é guiado pelo `Orchestrator`, que gerencia a comunicação sequencial entre os agentes:

1. **Entrada do Usuário**: A `CLI` recebe a descrição da tarefa (task).
2. **Orquestrador**: Inicializa o contador de tokens e a cadeia de agentes.
3. **Architect (Planejamento)**:
   - Recebe a `task`.
   - Utiliza a classe `LongChainReasoning` para estruturar a abordagem do problema antes da execução.
   - Produz a `architecture`.
4. **Coder (Implementação)**:
   - Recebe a `architecture`.
   - Produz o código inicial.
5. **Critic (Refinamento)**:
   - Recebe o `code`.
   - Analisa e gera sugestões e o feedback final.
6. **Saída**: O framework imprime os resultados e a quantidade total de tokens processados.

## Detalhes Técnicos de Alta Densidade

- **Long-Chain Reasoning**: A implementação isola a etapa de planejamento (em `core/reasoning.py`), permitindo que as decisões de arquitetura se baseiem em uma avaliação aprofundada prévia da tarefa.
- **Eficiência**: Projetado para gerenciar milhões de tokens ao modularizar tarefas. O `TokenCounter` funciona de forma autônoma acompanhando o custo computacional simulado de cada etapa.
- **Modelos Dedicados**: A integração via `MiMoClient` permite usar checkpoints diferentes, como `mimo-architect-v1`, `mimo-coder-v1` e `mimo-critic-v1`, especializando a IA para o papel designado.
