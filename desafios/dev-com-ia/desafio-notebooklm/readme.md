# Desafio: Criação de um Caderno Temático no NotebookLM

---

## Visão Geral

Este repositório apresenta materiais de estudo estruturados sobre **finanças pessoais para o investidor iniciante**, construídos a partir da análise de **14 artigos do Medium** e organizados em quatro camadas complementares:

| Arquivo | Propósito |
|---|---|
| `guia.md` | Guia teórico-acadêmico com referências |
| `prompts/prompt-study.md` | Copiloto socrático para estudo de conceitos |
| `prompts/prompt-plan.md` | Copiloto para diagnóstico e planejamento financeiro |
| `prompts/prompt-notebooklm.md` | 25 prompts estruturados para estudo via NotebookLM |

---

## Estrutura do Repositório

```
finance-study/
│
├── README.md                      ← Este arquivo
├── guia.md                        ← Guia acadêmico completo com referências
│
└── prompts/
    ├── prompt-study.md            ← Copiloto socrático para estudo de conceitos
    ├── prompt-plan.md             ← Copiloto para diagnóstico e planejamento financeiro
    └── prompt-notebooklm.md       ← Prompts para estudo via NotebookLM
```

---

## Tópicos Cobertos

### Value Investing — Benjamin Graham
- Contexto histórico e biográfico
- Valor intrínseco e análise fundamentalista
- Margem de segurança
- A metáfora de Mr. Market
- Distinção entre investimento e especulação
- Perfis de investidor: defensivo vs. empreendedor

### Sistema Financeiro Brasileiro — Renda Fixa
- Taxa Selic: Meta, efetiva e mecanismo do COPOM
- Tesouro Direto e Tesouro Selic
- Comparativo Poupança × Tesouro Selic
- CDB: estrutura, CDI e tabela regressiva de IR
- LCI e LCA: isenção fiscal e carências mínimas
- Metodologia de comparação CDB × LCI/LCA (rentabilidade líquida)
- FGC: cobertura e limites por CPF

### Planejamento Financeiro Pessoal
- Diagnóstico de situação atual (renda, dívidas, patrimônio, objetivos)
- Hierarquia de alocação: dívidas → emergência → médio prazo → longo prazo
- Construção e manutenção de reserva de emergência
- Gestão de risco de liquidez, crédito e mercado

---

## Como Usar Cada Arquivo

### `guia.md` — O Material Base

O guia é o ponto de partida. Leia-o em ordem, seguindo os tópicos do sumário. Cada seção segue a estrutura **DEFINIÇÃO → EXEMPLO → APLICAÇÃO**, com cálculos comentados, tabelas comparativas e referências acadêmicas.

Itens de atenção especial no guia:
- **Seção 2.2** — Os cinco pilares do Value Investing (núcleo filosófico)
- **Seção 3.6** — Metodologia de comparação CDB × LCI/LCA (núcleo técnico)
- **Seção 6** — Glossário de 18 termos essenciais
- **Seção 7** — Referências completas com links para todas as fontes

---

### `prompts/prompt-study.md` — Copiloto Socrático

Use para aprofundar qualquer conceito do guia com apoio de IA (Claude, ChatGPT, Gemini etc.).

**Como ativar:**
1. Abra seu assistente de IA
2. Cole o conteúdo de `prompt-study.md` como *system prompt* (instrução inicial)
3. Faça sua pergunta normalmente

**O copiloto de estudo:**
- Nunca entrega respostas diretas sem construir o raciocínio antes
- Calibra a profundidade da explicação pelo nível do operador
- Encerra toda resposta com uma pergunta socrática de verificação
- Apresenta cálculos como laboratórios comentados, não como receitas

**Exemplo:**
```
[system prompt: conteúdo de prompt-study.md]

Usuário: Qual a diferença entre CDB e LCI na prática?
```

---

### `prompts/prompt-plan.md` — Copiloto de Planejamento

Use para construir um plano de alocação baseado na sua situação financeira real.

**Como ativar:**
1. Abra seu assistente de IA
2. Cole o conteúdo de `prompt-plan.md` como *system prompt*
3. Responda ao **Formulário de Diagnóstico Inicial** que o copiloto apresentará

**O que o blueprint entrega:**
- Diagnóstico de vulnerabilidades (dívidas caras, ausência de reserva, alocação subótima)
- Hierarquia de prioridades fundamentada nos princípios de Graham
- Tabela de alocação com comparativo de rentabilidade líquida
- Calendário de implementação por fases (Alfa → Beta → Gama → Delta)
- Matriz de riscos com contramedidas práticas

> ⚠️ **Aviso:** Este copiloto não emite recomendações formais de investimento. O output é analítico e educacional. A decisão final é sempre do operador.

---

### `prompts/prompt-notebooklm.md` — Estudo via NotebookLM

Use para explorar o material de forma guiada e ancorada nas fontes originais, dentro do [NotebookLM](https://notebooklm.google.com) do Google.

**Como configurar o notebook:**
1. Acesse [notebooklm.google.com](https://notebooklm.google.com) e crie um novo notebook
2. Carregue `guia.md` como upload de arquivo
3. Adicione os artigos do Medium como URLs (lista completa em `prompt-notebooklm.md`)
4. Aguarde o processamento das fontes
5. Use os 25 prompts organizados em 5 módulos

**Os 5 módulos de estudo:**

| Módulo | Foco | Prompts |
|---|---|---|
| 1 — Orientação | Mapeamento e visão geral do material | NLM-01 a NLM-03 |
| 2 — Graham | Value Investing em profundidade progressiva | NLM-04 a NLM-09 |
| 3 — Renda Fixa | Mecanismos, cálculos e comparativos | NLM-10 a NLM-15 |
| 4 — Síntese | Conexões entre temas e revisão crítica | NLM-16 a NLM-20 |
| 5 — Materiais | Geração de glossários, roteiros e quizzes | NLM-21 a NLM-25 |

**Por que usar NotebookLM junto com os outros prompts?**

O NotebookLM ancora as respostas nas fontes carregadas — ideal para extração e estruturação do conhecimento com rastreabilidade. Os copilotos de IA (study e plan) vão além das fontes: aprofundam, calculam e adaptam ao contexto pessoal do operador. Os dois usos são complementares, não concorrentes.

```
NotebookLM       → O que as fontes dizem? (extração fiel)
prompt-study.md  → Por que funciona assim? (aprofundamento socrático)
prompt-plan.md   → Como isso se aplica à minha situação? (planejamento pessoal)
```

---

## Trilha de Estudo Recomendada

```
╔══════════════════════════════════════════════════════╗
║  FASE 1 — FUNDAÇÃO CONCEITUAL  (Semanas 1–2)         ║
╠══════════════════════════════════════════════════════╣
║  • Leia guia.md — Seções 1 e 2 (Graham)              ║
║  • NotebookLM: execute NLM-01, NLM-04, NLM-05        ║
║  • Exercício: identifique um exemplo de "Mr. Market" ║
║    no noticiário econômico desta semana               ║
╠══════════════════════════════════════════════════════╣
║  FASE 2 — RENDA FIXA  (Semana 3)                     ║
╠══════════════════════════════════════════════════════╣
║  • Leia guia.md — Seção 3 (Renda Fixa Brasileira)    ║
║  • NotebookLM: execute NLM-10 a NLM-14               ║
║  • Exercício: compare 3 CDBs e 2 LCIs disponíveis    ║
║    na sua corretora usando a fórmula do guia          ║
╠══════════════════════════════════════════════════════╣
║  FASE 3 — PRIMEIRO APORTE  (Semana 4)                ║
╠══════════════════════════════════════════════════════╣
║  • Abra conta no Tesouro Direto                       ║
║  • Faça o primeiro aporte em Tesouro Selic            ║
║  • Use prompt-study.md para tirar dúvidas do processo ║
╠══════════════════════════════════════════════════════╣
║  FASE 4 — PLANEJAMENTO  (Semanas 5–6)                 ║
╠══════════════════════════════════════════════════════╣
║  • Use prompt-plan.md para construir seu Blueprint    ║
║  • NotebookLM: execute NLM-16 e NLM-20 (síntese)     ║
╠══════════════════════════════════════════════════════╣
║  FASE 5 — CONSOLIDAÇÃO  (Semanas 7–8)                 ║
╠══════════════════════════════════════════════════════╣
║  • NotebookLM: execute NLM-19, NLM-24 (revisão ativa)║
║  • Elabore sua Declaração de Política de             ║
║    Investimento (IPS) pessoal                        ║
║  • Use prompt-study.md para revisar conceitos com    ║
║    dúvidas remanescentes                             ║
╚══════════════════════════════════════════════════════╝
```

---

## Referências das Fontes

Referências completas disponíveis em [`guia.md — Seção 7`](./guia.md#7-referências).

| Tema | Fonte |
|---|---|
| Value Investing — Graham | [Medium — Content Team](https://medium.com/@content_40548/the-father-of-value-investing-benjamin-graham-ba687acd7417) |
| The Intelligent Investor | [Medium — Quantum Oracle](https://medium.com/operations-research-bit/summary-of-the-intelligent-investor-by-benjamin-graham-5f175525cde8) |
| Princípios de Graham revisitados | [Medium — HedgeCo.app](https://medium.com/@hedgeco.app/the-art-of-value-investing-benjamin-grahams-principles-revisited-9cb04874b8e0) |
| Livros de Graham | [Medium — EventDrivenDaily](https://medium.com/@eventdrivendaily/books-written-by-benjamin-graham-timeless-lessons-for-modern-investors-cc0b0df3738e) |
| Taxa Selic explicada | [Medium — SenseInvest](https://medium.com/@senseinvest/tudo-o-que-voc%C3%AA-precisa-saber-sobre-taxa-selic-ddde73a2c44c) |
| Poupança vs. Tesouro Selic | [Medium — Blog Eu Rico](https://medium.com/@blog-eu-rico/poupan%C3%A7a-vs-tesouro-selic-qual-vale-mais-a-pena-940bc1215460) |
| Tesouro Selic explicado | [Medium — The Capital Advisor](https://medium.com/@thecapitaladvisor/o-que-%C3%A9-e-como-funciona-o-tesouro-selic-edd9579674e0) |
| CDB vs. CDI | [Medium — Paternidade](https://medium.com/paternidade/saiba-a-diferen%C3%A7a-entre-cdb-e-cdi-9838b94a2ac1) |
| Comparação CDB × LCI/LCA | [Medium — Fernando Kobuti](https://medium.com/@fernandokobuti/o-c%C3%A1lculo-para-comparar-cdb-lc-com-lci-lca-2b42399e6add) |
| CDB × LCI em Python | [Medium — Marcel Fraga](https://marcelfraga.medium.com/comparativo-rendimento-lci-lca-e-cdb-em-python-fb782bc0d654) |
| Guia LCI e LCA | [Medium — Compralo](https://usecompralo.medium.com/compraloexplica-guia-b%C3%A1sico-do-investidor-iniciante-lci-e-lca-991947a9bc2f) |
| IA e finanças pessoais | [Medium — UX by Leticia](https://uxbyleticia.medium.com/como-o-chatgpt-pode-te-ajudar-a-come%C3%A7ar-a-investir-mesmo-que-voc%C3%AA-n%C3%A3o-entenda-nada-sobre-isso-ad32719715c2) |
| Pequeno investidor inteligente | [Medium — Renato Fialho](https://medium.com/@renatofialho/criando-um-pequeno-investidor-inteligente-1a9918882611) |

---

## Notas

- Os prompts são compatíveis com qualquer assistente de IA baseado em chat (Claude, ChatGPT, Gemini etc.)
- O NotebookLM requer conta Google e aceita PDFs, textos e URLs como fontes
- As taxas mencionadas no `guia.md` são ilustrativas — consulte o [Banco Central](https://www.bcb.gov.br) e o [Tesouro Nacional](https://www.tesourodireto.com.br) para dados atualizados
- Este repositório é de caráter **exclusivamente educacional** e não constitui recomendação de investimento

---

*"O maior inimigo do investidor é, provavelmente, ele mesmo." — Benjamin Graham*