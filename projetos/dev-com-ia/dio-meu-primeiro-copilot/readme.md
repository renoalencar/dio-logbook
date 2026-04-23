# Repositório de Agentes Copilot

---

## 📋 Visão Geral

Este repositório é o **arquivo central de instrução** para os **Agentes Copilot**. Ele contém os prompts de sistema que definem o comportamento da entidade definida como**Dra. Lara Cruz**, uma arquiteta de sistemas autônoma injetada no fluxo de trabalho de desenvolvimento de software.

Cada arquivo nesta coleção representa um **modo operacional distinto**, um estado de raciocínio calibrado para uma função específica dentro do pipeline de engenharia: planejamento, execução, auditoria, refatoração e mentoria. A escolha do modo é responsabilidade do operador humano.

---

## 🧠 O que é um Agente Copilot?

Na teoria clássica de IA (Russell & Norvig), um **agente** é qualquer entidade que percebe seu ambiente via sensores e age sobre ele via atuadores. No paradigma de LLMs, um **Agente Copilot** representa a fusão entre:

- A **segurança assistiva** de um Copilot tradicional (Human-in-the-Loop)
- A **autonomia funcional** de um agente autônomo (Goal-Oriented Execution)

O resultado é uma entidade que pode executar fluxos de trabalho multifacetados enquanto mantém o operador humano como árbitro final de decisões críticas.

---

## 📁 Estrutura do Repositório

```
copilot-agents/
├── README.md                        ← Você está aqui
└── prompts/
    ├── prompt-agent.md              ← Modo AGENT: Geração de código de produção
    ├── prompt-ask.md                ← Modo ASK: Diagnóstico e consultoria (read-only)
    ├── prompt-edit.md               ← Modo EDIT: Refatoração cirúrgica de artefatos
    ├── prompt-plan.md               ← Modo PLAN: Blueprint arquitetural e mapeamento de risco
    └── prompt-study.md              ← Modo STUDY: Mentoria acadêmica e fundamentos
```

---

## ⚙️ Modos Operacionais

A entidade **Dra. Lara Cruz** opera em cinco modos distintos, cada um governado por seu próprio System Prompt. Selecione o modo conforme a natureza da tarefa.

| Modo | Arquivo | Função Principal | Autonomia de Código |
|------|---------|-----------------|-------------------|
| `AGENT` | `prompt-agent.md` | Geração de código de produção completo | ✅ Alta |
| `ASK` | `prompt-ask.md` | Diagnóstico, auditoria e consultoria técnica | ❌ Read-only |
| `EDIT` | `prompt-edit.md` | Refatoração cirúrgica de artefatos legados | ✅ Alta |
| `PLAN` | `prompt-plan.md` | Planejamento arquitetural e blueprints | ⚠️ Zero-code |
| `STUDY` | `prompt-study.md` | Mentoria, dissecação teórica e forja intelectual | 📚 Didático |

---

## 🔁 Fluxo de Trabalho Recomendado

O pipeline de engenharia ideal segue esta progressão de modos:

```
STUDY → PLAN → AGENT → EDIT → ASK
  ↑                              ↓
  └──────── Ciclo de Aprendizado ─┘
```

1. **STUDY** — Atua como um tutor que abarca os fundamentos do que será construído.
2. **PLAN** — Forja o blueprint arquitetural antes de escrever uma linha de código.
3. **AGENT** — Executa a síntese do código de produção.
4. **EDIT** — Refatora artefatos legados ou imperfeitos.
5. **ASK** — Audita, diagnostca anomalias e resolva dúvidas sem alterar o estado do sistema.

---

## 🚀 Como Usar

### 1. Selecione o Modo
Identifique qual modo operacional atende à sua necessidade atual no pipeline.

### 2. Carregue o Prompt
Copie o conteúdo do arquivo `.md` correspondente em `prompts/` e injete-o como **System Prompt** na sua interface de LLM (Copilot Studio, API Anthropic/OpenAI, ou qualquer orchestrator compatível).

### 3. Configure as Variáveis de Stack (Modo AGENT)
O `prompt-agent.md` contém **variáveis de template** que devem ser preenchidas antes do uso:

```
{NODE_VERSION}   → ex: "20.x LTS"
{FRAMEWORK}      → ex: "Express 4 / NestJS 10 / Fastify 4"
{MODULE_SYSTEM}  → ex: "ESM (ECMAScript Modules)"
{TEST_FRAMEWORK} → ex: "Vitest / Jest"
{LINT_FORMAT}    → ex: "ESLint + Prettier"
{DB}             → ex: "PostgreSQL + Prisma ORM"
{DEPLOY}         → ex: "Docker + GitHub Actions + Railway"
```

### 4. Inicie a Interação
A entidade iniciará a resposta com uma **constatação técnica direta**, sem saudações. Isso é intencional e faz parte do protocolo operacional.

---

## 🏗️ Arquitetura de Raciocínio (ReAct Framework)

Todos os modos foram projetados com base no framework **ReAct** (Yao et al., 2022 — *Synergizing Reasoning and Acting in Language Models*), que comprova que forçar o modelo a gerar traços de raciocínio explícito antes de executar ações reduz drasticamente as taxas de erro operacional.

```
Percepção (Input do Operador)
        ↓
   Raciocínio (Análise Crítica / Diagnóstico)
        ↓
   Ação (Código / Blueprint / Diagnóstico)
        ↓
   Observação (Validação / Alertas de Regressão)
        ↓
  Loop de Refinamento (Próxima diretriz)
```

---

## 🛡️ Guardrails e Boas Práticas

- **Nunca** use o Modo `AGENT` sem antes executar o Modo `PLAN` em sistemas críticos.
- **Sempre** revise os **Alertas de Regressão** emitidos pelo Modo `EDIT` antes de implantar.
- O Modo `ASK` é **read-only por design** — use-o quando precisar de diagnóstico sem risco de side-effects.
- Em sistemas com dados sensíveis, configure **OAuth 2.0** e delegação de permissões antes de ativar qualquer agente com acesso a APIs externas.

---

## 📚 Referências Técnicas

- **Russell, S. & Norvig, P.** — *Artificial Intelligence: A Modern Approach* (4th ed.)
- **Yao et al. (2022)** — [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- **OWASP Top 10** — [https://owasp.org/Top10/](https://owasp.org/Top10/)
- **Microsoft Copilot Studio** — [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)