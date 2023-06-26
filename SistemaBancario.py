import textwrap

def menu():
   menu = """\n
   ======================== MENU ===================
[ D ]\tDepositar
[ S ]\tSaque
[ E ]\tExtrato
[ NC ]\tNova conta
[ LC ]\tListar contas
[ NU ]\tNovo usuário
[ Q ]\tSair
=> """
   return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! o valor informado é inválido. @@@")
        return saldo, extrato

    def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\n@@@ Operação falhou! você não tem saldo suficiente. @@@")

        elif excedeu_limite:
            print("\n@@@ Operação falhou! o valor do saque excedeu o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! número máximo de saques excedeu. @@@")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! o valor informado é inválido. @@@")
        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ extrato ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\rR$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(só aceita números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF!. @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logadouro, número - bairro - cidade/sigra estado): ")

    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    agencia = input("Informe o código e o nome da agência: ")
    numero_conta = input("Informe o número da conta: ")
    usuario = input("Informe o nome do usuário e CPF: ")

    if agencia:
        print("\n@@@ Agência existente, informe o código corrreto!. @@@")
        return

    nome_agencia = input("Informe o nome da agência: ")
    data_abertura = input("Informe a data da abertura da conta(dd-mm-aaaa): ")
    endereco = input("Informe o endereço da agência(logadouro, número - bairro - cidade/sigra estado): ")
    print("=== Agência e conta criado com sucesso! ===")

    agencia.append({"nome_agencia": nome_agencia, "data_abertura": data_abertura, "endereço": endereco})
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Agencia e usuário não encontrado, fluxo de criação de conta encerrada ou inexistente! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Informe o valor do deposito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "Q":
            break

        else:
            print("Operação inválida, por favor digite outra opção válida.")
            print("Volte sempre e conte com os nossos serviços!")
main()
