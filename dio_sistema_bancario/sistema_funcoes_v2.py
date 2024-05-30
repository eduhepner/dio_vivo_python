import time

menu = """
####### MENU #######

[1] Saque
[2] Depósito
[3] Extrato
[4] Criar usuário
[5] Criar conta-corrente
[6] Listar contas
[0] Sair

>>> """

saldo = float(0)
extrato = ""
numero_saques = 0
limite_saques = 3
limite = 500
agencia = "0001"
conta = 0
todas_contas = {}
lista_usuarios = {}


def sacar(*, saldo, valor, limite, limite_saques, numero_saques,extrato):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor <= saldo and valor > limite:
        print("Limite máximo de R$ 500,00 por saque.")   
    elif valor <= 0:
        print("Valor inválido.")
    else:
        numero_saques += 1
        saldo -= valor
        print(f"""Sacando R$ {valor:.2f}.
Seu saldo agora é de R${saldo:.2f}.""")
        extrato += f"--- Operação de saque no valor de R$ {valor:.2f}.\n"
        if numero_saques < limite_saques:
            print(f"Você pode fazer mais {limite_saques - numero_saques} saque(s).")
        else:
            print("Você chegou no seu limite de saques por hoje.")
    return saldo, numero_saques, extrato


def deposito(saldo, valor, extrato, /):
    if valor < 0:
            print("Valor inválido.")
    else:
        saldo += valor
        print(f"""Depositando R$ {valor:.2f}.
Seu saldo agora é de R${saldo:.2f}.""")
        extrato += f"+++ Operação de depósito no valor de R$ {valor:.2f}.\n"
    return (saldo, extrato)


def gerar_extrato(saldo, / , *, extrato):
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print("   EXTRATO   ".center(50, "#"))
        print(f"""\n{extrato}
Saldo Atual: R$ {saldo:.2f}\n""")
        print("".center(50, "#"))


def criar_usuario(lista_usuarios,):
    cpf = input("""Informe seu CPF (somente números) ou [0] para voltar:
>>> """)
    if cpf == "0":
        return lista_usuarios
    elif len(cpf) != 11 or not cpf.isdigit():
        print("""CPF inválido. Digite somente os 11 números.""")
        return lista_usuarios
    elif lista_usuarios and any(usuario == cpf for usuario in lista_usuarios):
        print("CPF já cadastrado!")
        return lista_usuarios
    else:
        nome = input("""Digite seu nome e sobrenome:
>>> """)
        if nome == "":
            print("Nome inválido.")
            return lista_usuarios
        data = input("""Digite sua data de nascimento (DD/MM/AAAA):
>>> """)
        if data == "":
            print("Data inválida.")
            return lista_usuarios
        endereco = input("""Digite seu endereço na forma "logradouro, número -  bairro - cidade/sigla do estado:"
>>> """)
        if endereco == "":
            print("Endereço inválido.")
            return lista_usuarios
        usuario = {"Nome" : nome, "Data" : data, "Endereço" : endereco}
        lista_usuarios[cpf] = usuario
        print(lista_usuarios)
        return lista_usuarios

def criar_conta(conta, agencia, lista_usuarios, todas_contas):
    cpf = input("""Digite seu CPF:
>>> """)
    if lista_usuarios and any(usuario == cpf for usuario in lista_usuarios):
        conta += 1
        conta_corrente = f"{agencia}-{conta}"
        todas_contas[conta_corrente] = {cpf: lista_usuarios[cpf]}
        print(todas_contas)
        print(f"""Conta criada com sucesso!
{conta_corrente} - {todas_contas[conta_corrente][cpf]['Nome']}""")
        return todas_contas, conta
    else:
        print("CPF não encontrado.")
        return todas_contas, conta
    
def lista_contas(todas_contas):
    if todas_contas:
        for chave, valor in todas_contas.items():
            print("=" * 50)
            print(f"""Agência: {chave[:4]}
Conta: {chave[5:]}""")
            for usuario in valor.values():
                print(f"Nome: {usuario['Nome']}")
    else:
        print("Nenhuma conta criada até o momento.")
        return todas_contas
    

while True:
    time.sleep(2)
    opcao = input(menu)
    if not opcao.isdigit() or int(opcao) > 6:
        print("Operação inválida, por favor selecione uma das opções.")
    elif opcao == "1":
        if numero_saques >= limite_saques:
                print("Você já fez o número máximo de saques!")
        else:
            valor = input("Digite o valor que deseja sacar: R$ ")
            if valor.isdigit():
                valor = float(valor)

                saldo, numero_saques, extrato = sacar(
                saldo=saldo, 
                limite_saques=limite_saques, 
                valor=valor, 
                limite=limite, 
                numero_saques=numero_saques, 
                extrato=extrato,
                )

            else:
                print("Valor inválido.")
            
    elif opcao == "2":
        valor = input("Digite o valor que deseja depositar: R$ ")
        if valor.isdigit():
            valor = float(valor)
            saldo, extrato = deposito(saldo, valor, extrato)
        else:
            print("Valor inválido.")
    elif opcao == "3":
        gerar_extrato(saldo, extrato=extrato)
    elif opcao == "4":
        print(lista_usuarios)
        lista_usuarios = criar_usuario(lista_usuarios)
    elif opcao == "5":
        todas_contas, conta = criar_conta(conta, agencia, lista_usuarios, todas_contas)
    elif opcao == "6":
        lista_contas(todas_contas)
    else:
        opcao == "0"
        break