# 💰 Sistema Bancário em Python

Este projeto implementa um sistema bancário simples em Python com operações básicas de depósito, saque e extrato.

## 🎯 Funcionalidades Implementadas

### ✅ Operação de Depósito
- Aceita apenas valores positivos
- Armazena todos os depósitos para exibição no extrato
- Atualiza o saldo da conta automaticamente

### ✅ Operação de Saque
- Limite de 3 saques diários
- Valor máximo de R$ 500,00 por saque
- Verificação de saldo disponível
- Armazena todos os saques para exibição no extrato

### ✅ Operação de Extrato
- Lista completa de todos os depósitos e saques
- Exibe o saldo atual da conta
- Formata os valores no padrão monetário brasileiro (R$ XXX.XX)

## 🏦 Estrutura do Projeto

```python
# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
```

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/renoalencar/dio-logbook.git
```

2. Navegue até o diretório:
```bash
cd desafios/python/00-fundamentos/sistema-bancario-py-v01
```

3. Execute o programa:
```bash
python sistema-bancario-py-v01.py
```

## 📋 Menu de Operações

```
=============== MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=====================================
```

## 💻 Exemplo de Uso

### Depósito:
```
Informe o valor do depósito: 350.50
Depósito de R$ 350.50 realizado com sucesso!
```

### Saque:
```
Informe o valor do saque: 200.00
Saque de R$ 200.00 realizado com sucesso!
```

### Extrato:
```
=============== EXTRATO ================
Depósito: R$ 350.50
Saque:    R$ 200.00

----------------------------------------
Saldo:    R$ 150.50
========================================
```

## ⚠️ Regras de Negócio Implementadas

- ❌ **Saques sem saldo**: "Operação falhou! Saldo insuficiente."
- ❌ **Saques acima do limite**: "Operação falhou! Valor excede o limite de R$ 500.00 por saque."
- ❌ **Excesso de saques**: "Operação falhou! Número máximo de saques excedido (3 por dia)."
- ❌ **Valores inválidos**: "Operação falhou! Valor informado é inválido."

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **Estruturas de controle** - Loops e condicionais
- **Formatação de strings** - Para exibição monetária

## 👨‍💻 Autor

Desenvolvido como parte do desafio de programação da Digital Innovation One.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](dio-logbook/LICENSE) para mais detalhes.

---

**💡 Observação**: Este sistema foi desenvolvido como uma versão inicial (v1) para um único usuário, sem identificação de agência e conta, conforme especificado no desafio.