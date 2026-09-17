from banco import acessar_conta, cadastrar_conta, mostrar_saldo
from boletos import agendar_boleto, liquidar_pagamentos, ver_fila
from operacoes import depositar, estornar, mostrar_extrato, pix, sacar


def menu_conta(conta):
    while True:
        print(f"\n=== Conta {conta['numero']} - {conta['nome']} ===")
        print("1 - Consultar saldo\n2 - Depositar\n3 - Sacar\n4 - Pix\n"
              "5 - Ver extrato\n6 - Estornar ultima transacao\n7 - Agendar boleto\n"
              "8 - Ver fila de boletos\n9 - Liquidar pagamentos\n10 - Voltar")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            mostrar_saldo(conta)
        elif opcao == "2":
            depositar(conta)
        elif opcao == "3":
            sacar(conta)
        elif opcao == "4":
            pix(conta)
        elif opcao == "5":
            mostrar_extrato(conta)
        elif opcao == "6":
            estornar(conta)
        elif opcao == "7":
            agendar_boleto(conta)
        elif opcao == "8":
            ver_fila(conta)
        elif opcao == "9":
            liquidar_pagamentos(conta)
        elif opcao == "10":
            break
        else:
            print("Opcao invalida.")


def menu_inicial():
    while True:
        print("\n=== ByteBank ===")
        print("1 - Cadastrar conta\n2 - Acessar conta\n3 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            cadastrar_conta()
        elif opcao == "2":
            conta = acessar_conta()
            if conta is None:
                print("Conta nao encontrada.")
            else:
                menu_conta(conta)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")


menu_inicial()
