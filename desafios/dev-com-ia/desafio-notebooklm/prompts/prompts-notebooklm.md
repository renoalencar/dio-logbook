# Prompts para NotebookLM — Estudo em Finanças Pessoais e Value Investing

> **Ferramenta:** [NotebookLM](https://notebooklm.google.com) (Google)  
> **Modo de uso:** Cole cada prompt na caixa de chat do NotebookLM após carregar as fontes indicadas  
> **Fontes recomendadas:** `guia.md` + artigos do Medium listados em `guia.md#7-referências`

---

## O que é o NotebookLM e por que usá-lo aqui

O NotebookLM é uma ferramenta do Google que permite fazer perguntas diretamente sobre um conjunto de documentos carregados pelo usuário — sem que o modelo "invente" informações de fora das fontes. Isso o torna ideal para estudo orientado por material: as respostas são ancoradas no que você leu, não em dados genéricos da internet.

**Fluxo recomendado de configuração:**

1. Acesse [notebooklm.google.com](https://notebooklm.google.com) e crie um novo notebook
2. Carregue as fontes (veja seção abaixo)
3. Aguarde o processamento das fontes
4. Use os prompts desta página em ordem crescente de complexidade

---

## Fontes para Carregar no Notebook

Carregue os materiais na seguinte ordem de prioridade:

### Fonte Primária (obrigatória)
- `guia.md` — O guia acadêmico deste repositório

### Fontes Secundárias — Value Investing (adicione como URLs)
- https://medium.com/@content_40548/the-father-of-value-investing-benjamin-graham-ba687acd7417
- https://medium.com/operations-research-bit/summary-of-the-intelligent-investor-by-benjamin-graham-5f175525cde8
- https://medium.com/@hedgeco.app/the-art-of-value-investing-benjamin-grahams-principles-revisited-9cb04874b8e0
- https://medium.com/@eventdrivendaily/books-written-by-benjamin-graham-timeless-lessons-for-modern-investors-cc0b0df3738e

### Fontes Secundárias — Renda Fixa Brasileira (adicione como URLs)
- https://medium.com/@senseinvest/tudo-o-que-voc%C3%AA-precisa-saber-sobre-taxa-selic-ddde73a2c44c
- https://medium.com/@blog-eu-rico/poupan%C3%A7a-vs-tesouro-selic-qual-vale-mais-a-pena-940bc1215460
- https://medium.com/@thecapitaladvisor/o-que-%C3%A9-e-como-funciona-o-tesouro-selic-edd9579674e0
- https://medium.com/@fernandokobuti/o-c%C3%A1lculo-para-comparar-cdb-lc-com-lci-lca-2b42399e6add
- https://usecompralo.medium.com/compraloexplica-guia-b%C3%A1sico-do-investidor-iniciante-lci-e-lca-991947a9bc2f
- https://medium.com/paternidade/saiba-a-diferen%C3%A7a-entre-cdb-e-cdi-9838b94a2ac1
- https://marcelfraga.medium.com/comparativo-rendimento-lci-lca-e-cdb-em-python-fb782bc0d654

### Fontes Secundárias — IA e Iniciantes
- https://uxbyleticia.medium.com/como-o-chatgpt-pode-te-ajudar-a-come%C3%A7ar-a-investir-mesmo-que-voc%C3%AA-n%C3%A3o-entenda-nada-sobre-isso-ad32719715c2
- https://medium.com/@renatofialho/criando-um-pequeno-investidor-inteligente-1a9918882611

> **Dica:** O NotebookLM aceita até 50 fontes por notebook. Se alguma URL do Medium exigir login para acesso, salve o artigo como PDF e faça upload do arquivo diretamente.

---

## MÓDULO 1 — Orientação e Mapeamento do Material

*Use estes prompts antes de começar o estudo. O objetivo é construir um mapa mental do que está disponível nas fontes.*

---

### NLM-01 · Visão Geral do Material

```
Analise todas as fontes carregadas e me apresente um panorama geral do que está coberto.
Organize a resposta em três blocos:

1. Quais são os principais temas abordados no conjunto de fontes?
2. Quais fontes tratam de Value Investing e Benjamin Graham?
3. Quais fontes tratam de produtos financeiros brasileiros (Selic, CDB, LCI, LCA)?

Para cada bloco, indique de qual fonte a informação foi retirada.
```

---

### NLM-02 · Mapa de Conceitos

```
Com base em todas as fontes, liste todos os conceitos financeiros mencionados, 
do mais básico ao mais avançado. Para cada conceito:

- Dê uma definição em uma frase, conforme aparece nas fontes
- Indique em qual(is) fonte(s) ele é explicado
- Classifique como: [FUNDAMENTAL] / [INTERMEDIÁRIO] / [AVANÇADO]

Organize a lista em ordem crescente de complexidade.
```

---

### NLM-03 · Identificação de Lacunas

```
Após analisar todas as fontes, responda:

1. Quais tópicos são cobertos com profundidade (múltiplas fontes concordando)?
2. Quais tópicos são mencionados superficialmente (apenas uma fonte, sem exemplos)?
3. Existe algum conceito referenciado em uma fonte que não é explicado em nenhuma outra?

Use esta análise para me ajudar a priorizar o que estudar com atenção e o que 
precisarei buscar em materiais externos.
```

---

## MÓDULO 2 — Benjamin Graham e Value Investing

*Prompts de aprofundamento progressivo. Recomenda-se usá-los em ordem.*

---

### NLM-04 · Fundação Biográfica e Contexto Histórico

```
Com base nas fontes, descreva o contexto histórico que levou Benjamin Graham 
a desenvolver o Value Investing. 

Responda: Quais eventos da vida de Graham moldaram sua filosofia? 
Por que o crash de 1929 foi determinante para seu método?
Que problema do mercado financeiro da época ele estava tentando resolver?

Cite as fontes específicas que embasam cada parte da resposta.
```

---

### NLM-05 · Os Cinco Pilares do Value Investing

```
As fontes descrevem os princípios fundamentais do Value Investing de Graham.
Extraia e explique cada um desses princípios, respondendo para cada um:

a) O que é o princípio?
b) Qual problema ele resolve para o investidor?
c) Como ele se aplica na prática — existe algum exemplo nas fontes?
d) Em quais fontes este princípio aparece?

Ao final, ordene os princípios do mais básico ao mais sofisticado.
```

---

### NLM-06 · Dissecando o Mr. Market

```
A metáfora do "Mr. Market" é central na filosofia de Graham. 
Com base nas fontes:

1. Explique a metáfora com suas próprias palavras, a partir do que as fontes dizem
2. Qual é o erro que o investidor comum comete em relação ao Mr. Market?
3. Como o investidor inteligente deveria se comportar diante do Mr. Market?
4. Esta metáfora se aplica ao mercado brasileiro de renda fixa? 
   Construa um exemplo hipotético usando os produtos mencionados nas fontes.

Indique de qual fonte cada parte da resposta foi extraída.
```

---

### NLM-07 · Margem de Segurança — Da Teoria à Renda Fixa

```
O conceito de "margem de segurança" de Graham foi desenvolvido para ações,
mas as fontes sugerem que ele pode ser aplicado mais amplamente.

Responda com base nas fontes:
1. Como as fontes definem margem de segurança?
2. Qual é o mecanismo que faz a margem de segurança proteger o investidor?
3. Como o conceito de "custo de oportunidade" mencionado nas fontes sobre a Selic
   pode ser entendido como uma forma de margem de segurança na renda fixa?

Se as fontes não respondem diretamente ao item 3, indique isso explicitamente
e apresente o que as fontes dizem sobre cada parte separadamente.
```

---

### NLM-08 · Investimento vs. Especulação — Teste de Classificação

```
Graham define com precisão a diferença entre investimento e especulação.
Com base nas fontes:

1. Qual é a definição exata (ou mais próxima) de investimento segundo Graham?
2. Qual é a definição de especulação?
3. Agora classifique cada um dos itens abaixo como INVESTIMENTO ou ESPECULAÇÃO 
   segundo a lógica das fontes, justificando cada resposta:

   a) Comprar Tesouro Selic e manter por 2 anos
   b) Comprar CDB de banco pequeno atraído pela taxa alta sem pesquisar o emissor
   c) Aportar mensalmente em LCI com prazo definido e objetivo de compra de imóvel
   d) Resgatar um CDB antes do prazo por medo de uma notícia negativa
   e) Diversificar entre Tesouro Selic, CDB e LCA conforme a metodologia das fontes

Cite as partes das fontes que fundamentam cada classificação.
```

---

### NLM-09 · Graham Aplicado ao Brasil Atual

```
Graham escreveu para o mercado americano do século XX. As fontes fazem alguma 
ponte entre os princípios dele e o mercado brasileiro atual?

1. Quais princípios de Graham as fontes explicitamente aplicam ao contexto brasileiro?
2. Onde essa ponte não é feita diretamente — quais princípios ficaram sem equivalente nacional?
3. Com base no que as fontes dizem sobre a Taxa Selic e o custo de oportunidade,
   como você descreveria o "valor intrínseco" de um produto de renda fixa no Brasil?

Seja claro sobre o que está nas fontes e o que é inferência lógica.
```

---

## MÓDULO 3 — Renda Fixa Brasileira

*Prompts focados na camada técnica: mecanismos, cálculos e comparativos.*

---

### NLM-10 · O Mecanismo da Selic do Zero

```
Imagine que você precisa explicar a Taxa Selic para alguém que nunca ouviu falar 
em economia. Com base exclusivamente nas fontes carregadas:

1. O que é a Taxa Selic e para que ela serve?
2. Quem define a Selic e como esse processo funciona?
3. Qual é a diferença entre Selic, Selic Meta e Tesouro Selic?
4. Como a Selic afeta a vida cotidiana de quem não investe?

Use linguagem simples. Indique de qual fonte cada parte da explicação vem.
```

---

### NLM-11 · Poupança vs. Tesouro Selic — O Veredicto das Fontes

```
As fontes comparam diretamente a poupança e o Tesouro Selic.
Estruture um veredicto completo respondendo:

1. Como funciona a regra de remuneração da poupança segundo as fontes?
2. Em que condição a poupança perde para o Tesouro Selic, mesmo sendo isenta de IR?
3. Em que cenário (se existir) a poupança seria preferível?
4. As fontes apresentam algum cálculo numérico comparativo? Se sim, reproduza-o.
5. Qual é a conclusão final que as fontes chegam sobre este comparativo?

Ao final, sintetize em uma frase: "Para quem tem R$ X disponível e horizonte de Y,
a melhor opção segundo as fontes é Z porque..."
```

---

### NLM-12 · CDB — Anatomia Completa

```
Com base nas fontes, construa uma explicação completa do CDB cobrindo:

1. O que é e como funciona o CDB (mecanismo de emissão e remuneração)
2. O que é o CDI e por que o CDB é expresso como % do CDI
3. Como funciona a tabela regressiva do IR — por que ela existe e como impacta o retorno
4. O que é o FGC e qual proteção ele oferece ao investidor em CDB
5. Quais são os principais riscos de um CDB que as fontes mencionam?

Para cada item, cite a fonte de onde a informação foi retirada.
```

---

### NLM-13 · LCI e LCA — O Mito da Isenção

```
Existe um "mito" sobre LCI e LCA mencionado nas fontes. Identifique-o e 
construa uma análise completa respondendo:

1. Qual é o mito sobre LCI/LCA que as fontes explicitamente desmistificam?
2. Como funciona a metodologia correta de comparação CDB × LCI/LCA?
3. Reproduza os exemplos numéricos que as fontes apresentam, passo a passo
4. Quando a LCI/LCA vence o CDB? Quando o CDB vence?
5. O que muda nesta comparação conforme o prazo aumenta?

Apresente a fórmula de equivalência mencionada nas fontes e explique cada variável.
```

---

### NLM-14 · Simulação Comparativa Guiada

```
Com base na metodologia de comparação descrita nas fontes, me ajude a 
construir três cenários hipotéticos diferentes onde o resultado da comparação
CDB × LCI/LCA muda:

Cenário A: Prazo curto (até 6 meses) — quem tende a vencer e por quê?
Cenário B: Prazo médio (1 a 2 anos) — como o resultado muda?
Cenário C: Prazo longo (acima de 2 anos) — qual é a dinâmica aqui?

Para cada cenário, use a fórmula das fontes e explique a lógica por trás do resultado.
Ao final, proponha uma "regra de bolso" que resuma quando escolher cada produto.
```

---

### NLM-15 · Mapa de Risco dos Produtos

```
As fontes mencionam diferentes tipos de risco associados a cada produto de renda fixa.
Construa uma tabela de risco mapeando para cada produto (Poupança, Tesouro Selic, CDB, LCI, LCA):

- Risco de crédito (quem garante o pagamento?)
- Risco de liquidez (posso resgatar quando precisar?)
- Risco de mercado (o valor oscila?)
- Cobertura do FGC (sim/não e em qual limite?)

Ao final, responda: segundo as fontes, qual produto tem o menor risco total para 
um investidor que precisa de liquidez imediata?
```

---

## MÓDULO 4 — Síntese, Conexões e Revisão Crítica

*Prompts para consolidar o aprendizado e identificar conexões entre os temas.*

---

### NLM-16 · Conexão Transversal — Graham e Renda Fixa

```
Este prompt explora conexões que as fontes podem não fazer explicitamente.

Com base em tudo que as fontes dizem sobre Graham E sobre renda fixa brasileira,
responda:

1. Como o conceito de "margem de segurança" de Graham se manifesta na decisão 
   de manter uma reserva de emergência em Tesouro Selic?

2. Como o comportamento do "Mr. Market" se traduz para o investidor que resgata 
   um CDB antes do prazo por medo de notícias negativas?

3. Como a lógica de "valor intrínseco" se aplica à análise de um CDB versus 
   uma LCI quando usamos a metodologia de rentabilidade líquida?

Seja explícito sobre o que está nas fontes e o que é sua inferência a partir delas.
```

---

### NLM-17 · Auditoria de Consistência entre Fontes

```
As fontes foram escritas por autores diferentes, em momentos diferentes.
Faça uma auditoria de consistência respondendo:

1. Existe algum ponto em que duas ou mais fontes apresentam informações 
   contraditórias ou diferentes sobre o mesmo tema?

2. Existe alguma fonte que apresenta uma afirmação que não é corroborada 
   por nenhuma outra fonte do notebook?

3. Existe algum conceito que uma fonte explica de forma mais completa ou 
   precisa do que as outras?

Esta análise me ajuda a saber em quais fontes depositar mais confiança.
```

---

### NLM-18 · Perguntas que as Fontes Não Respondem

```
Com base em tudo que as fontes cobrem, identifique:

1. Quais perguntas práticas de um investidor iniciante brasileiro as fontes 
   NÃO respondem diretamente?

2. Quais conceitos são mencionados mas não explicados nas fontes 
   (ex.: termos usados sem definição)?

3. Quais seriam os próximos tópicos lógicos de estudo após dominar 
   o conteúdo das fontes atuais?

Use esta resposta para montar uma lista de tópicos para estudo futuro.
```

---

### NLM-19 · Flashcard Socrático — Revisão Ativa

```
Crie 10 perguntas de revisão baseadas exclusivamente no conteúdo das fontes,
cobrindo os três temas principais: Graham, Renda Fixa e Planejamento.

Para cada pergunta:
- Formule a pergunta de forma que exija raciocínio, não memorização
- Indique de qual fonte o conteúdo necessário para responder foi retirado
- Classifique a dificuldade: [BÁSICO] / [INTERMEDIÁRIO] / [AVANÇADO]

Após apresentar as 10 perguntas, aguarde minha resposta para a primeira antes 
de revelar a resposta esperada pelas fontes.
```

---

### NLM-20 · Síntese Final — O Investidor que as Fontes Descrevem

```
Imagine o investidor ideal que emerge do conjunto completo das fontes —
alguém que aplicou todos os princípios de Graham E domina todos os 
produtos de renda fixa brasileiros descritos.

Com base nas fontes, descreva este investidor em termos de:

1. Como ele pensa sobre o mercado (filosofia e mentalidade)
2. Como ele toma decisões de alocação (processo e metodologia)
3. Quais erros ele nunca comete (e por quê, segundo as fontes)
4. Qual seria sua alocação típica de carteira, segundo os princípios das fontes

Ao final, identifique: qual é a diferença mais fundamental entre este investidor 
e o investidor mediano que as fontes implicitamente criticam?
```

---

## MÓDULO 5 — Geração de Material de Estudo

*Prompts para criar materiais derivados a partir das fontes — resumos, tabelas, roteiros.*

---

### NLM-21 · Glossário Derivado das Fontes

```
Extraia de todas as fontes todos os termos técnicos financeiros que aparecem,
mesmo que sem definição explícita. Para cada termo:

- Apresente a definição conforme a fonte a apresenta (ou a melhor inferência dentro das fontes)
- Indique em qual(is) fonte(s) o termo aparece
- Marque com ⭐ os termos que você considera essenciais para compreender o material

Organize em ordem alfabética e formate como uma tabela com três colunas:
Termo | Definição (conforme fontes) | Fonte(s)
```

---

### NLM-22 · Roteiro de Podcast — Episódio sobre Graham

```
Com base nas fontes sobre Benjamin Graham, crie um roteiro de podcast 
de 10 minutos para um episódio intitulado: 
"Benjamin Graham: o homem que ensinou Warren Buffett a investir"

O roteiro deve ter:
- Abertura com gancho (30 segundos)
- Contexto histórico (2 minutos)
- Os 3 princípios mais importantes de Graham, explicados de forma acessível (5 minutos)
- Aplicação prática para o ouvinte brasileiro hoje (2 minutos)
- Encerramento com chamada para reflexão (30 segundos)

Use apenas informações presentes nas fontes. Indique entre colchetes [FONTE: X] 
cada informação usada.
```

---

### NLM-23 · Resumo Executivo — Uma Página por Tema

```
Crie três resumos executivos de uma página (máximo 300 palavras cada), 
um para cada tema principal das fontes:

RESUMO 1 — "Value Investing de Graham em 300 palavras"
RESUMO 2 — "Renda Fixa Brasileira em 300 palavras"  
RESUMO 3 — "Como começar a investir: o passo a passo das fontes em 300 palavras"

Cada resumo deve ser autocontido — alguém que leia apenas aquele resumo 
deve ter uma visão completa do tema. Use apenas informações das fontes.
```

---

### NLM-24 · Quiz de Múltipla Escolha — Verificação de Aprendizado

```
Crie um quiz de 15 questões de múltipla escolha (4 alternativas cada) 
cobrindo os conteúdos das fontes. 

Requisitos:
- 5 questões sobre Graham e Value Investing
- 5 questões sobre mecanismos da Selic, CDB, LCI e LCA
- 5 questões sobre comparativos e cálculos (com números hipotéticos)

Para cada questão:
- Apresente a pergunta e as 4 alternativas (A, B, C, D)
- Indique entre colchetes [RESPOSTA: X] ao final de cada questão
- Indique de qual fonte o conteúdo foi extraído

Apresente todas as questões antes de revelar as respostas.
```

---

### NLM-25 · Plano de Revisão Espaçada

```
Com base em todos os conceitos identificados nas fontes, crie um plano de 
revisão espaçada para 4 semanas seguindo a lógica do método Leitner:

Semana 1 — Conceitos novos: o que estudar e em que ordem?
Semana 2 — Primeira revisão + novos conceitos intermediários
Semana 3 — Revisão reforçada dos conceitos com dificuldade + avançados
Semana 4 — Revisão completa + exercícios de aplicação

Para cada semana, indique:
- Quais conceitos revisar (com referência à fonte)
- Uma pergunta de auto-avaliação para cada conceito
- Um exercício prático (cálculo ou análise) baseado nas fontes
```

---

## Dicas de Uso Avançado no NotebookLM

### Estratégia de Sessão de Estudo

Uma sessão eficiente segue esta sequência:

```
1. Sessão de Orientação (15 min)
   → Use NLM-01, NLM-02

2. Sessão de Aprofundamento (30–45 min)
   → Escolha um módulo (2, 3 ou 4) e percorra os prompts em ordem

3. Sessão de Síntese (15 min)
   → Use NLM-16 ou NLM-20 para conectar o que aprendeu

4. Sessão de Revisão (20 min)
   → Use NLM-19 ou NLM-24 para testar retenção
```

### Combinando com os Outros Prompts do Repositório

O NotebookLM é ideal para **extração e estruturação** do conhecimento das fontes. Para **aprofundamento socrático** e **planejamento pessoal**, combine com:

- `prompt-study.md` → após identificar um conceito no NotebookLM que você quer entender melhor, leve a dúvida para um assistente de IA com o prompt de estudo
- `prompt-plan.md` → após o estudo, use o prompt de planejamento para aplicar os conceitos à sua situação financeira real

### Limitações a Conhecer

| Limitação | Como contornar |
|---|---|
| NotebookLM não faz cálculos em tempo real | Leve os dados para uma calculadora ou para um assistente como Claude |
| Artigos do Medium podem exigir login | Salve como PDF e faça upload direto |
| Respostas longas podem ser truncadas | Peça para o notebook "continuar" ou divida o prompt em partes menores |
| O notebook não acessa URLs externas nas respostas | Todas as informações devem estar nas fontes carregadas |

---

*Estes prompts foram projetados para uso com o `guia.md` e os artigos listados em `guia.md#7-referências`. Para melhores resultados, carregue todas as fontes antes de iniciar o estudo.*