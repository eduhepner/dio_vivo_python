import time

menu = """
####### MENU #######

[1] Saque
[2] Depósito
[3] Extrato
[0] Sair

>>> """

saldo = float(0)
extrato = ""
numero_saques = 0
limite_saques = 3
limite = 500


while True:
    time.sleep(2)
    opcao = int(input(menu))
    if opcao == 1:
        if numero_saques >= limite_saques:
                print("Você já fez o número máximo de saques!")
                continue    
        else:
            valor = float(input("Digite o valor que deseja sacar: R$ "))
            
            if valor > saldo:
                print("Saldo insuficiente.")
                continue
            elif valor <= saldo and valor > limite:
                print("Limite máximo de R$ 500,00 por saque.")   
            elif valor <= 0:
                print("Valor inválido.")
            else:
                numero_saques += 1
                saldo -= valor
                print(f"""Sacando R$ {valor:.2f}.
Seu saldo agora é de R${saldo:.2f}.
""")
                if numero_saques < limite_saques:
                    print(f"Você pode fazer mais {limite_saques - numero_saques} saque(s).")
                else:
                    print("Você chegou no seu limite de saques por hoje.")
                extrato += f"--- Operação de saque no valor de R$ {valor:.2f}.\n"
                continue
    elif opcao == 2:
        deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if deposito < 0:
                print("Valor inválido.")
        else:
            saldo += deposito
            print(f"""Depositando R$ {deposito:.2f}.
Seu saldo agora é de R${saldo:.2f}.""")
            extrato += f"+++ Operação de depósito no valor de R$ {deposito:.2f}.\n"
            continue
    elif opcao == 3:
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(f"""\n##############  EXTRATO  ##############
{extrato}
Saldo Atual: R$ {saldo:.2f}
#######################################\n""")
    elif opcao == 0:
        break
    else:
        print("Operação inválida, por favor selecione uma das opções.")
