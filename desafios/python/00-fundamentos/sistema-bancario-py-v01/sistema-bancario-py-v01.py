menu = """
=============== MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=====================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    operacao = input(menu)

    if operacao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!\n")
        else:
            print("Operação falhou! O valor informado é inválido.\n")

    elif operacao == "s":
        valor = float(input("Informe o valor do saque: "))

        if 0 < valor <= saldo and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Você atingiu o limite de saques.\n")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.\n")
        else:
            print("Operação falhou! Valor informado é inválido.\n")

    elif operacao == "e":
        print("\n=============== EXTRATO ================")
        print(f"Não foram realizadas movimentações." if not extrato else extrato)
        print("----------------------------------------")
        print(f"Saldo: R$ {saldo:.2f}")
        print("========================================\n")

    elif operacao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida! Por favor, escolha uma opção válida.")