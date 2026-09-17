from banco import acessar_conta, cadastrar_conta, mostrar_saldo
from boletos import agendar_boleto, liquidar_pagamentos, ver_fila
from cofrinhos import (criar_cofrinho, guardar_no_cofrinho, resgatar_do_cofrinho,
                       simular_rendimento, ver_cofrinhos)
from credito import comprar_no_credito, pagar_fatura, ver_fatura
from emprestimos import (contratar_emprestimo, pagar_parcela_emprestimo,
                         simular_emprestimo)
from moedas import comprar_moeda_estrangeira, vender_moeda_estrangeira, ver_carteira
from operacoes import depositar, estornar, mostrar_extrato, pix, sacar
from pontos import consultar_pontos, resgatar_cashback
from relatorio import relatorio_categoria


def menu_conta(conta):
    while True:
        print(f"\n=== Conta {conta['numero']} - {conta['nome']} ===")
        print("1 - Consultar saldo\n2 - Depositar\n3 - Sacar\n4 - Pix\n"
              "5 - Ver extrato\n6 - Estornar ultima transacao\n7 - Agendar boleto\n"
              "8 - Ver fila de boletos\n9 - Liquidar pagamentos\n"
              "10 - Relatorio por categoria\n11 - Consultar pontos\n"
              "12 - Resgatar cashback\n13 - Criar caixinha\n"
              "14 - Guardar na caixinha\n15 - Resgatar da caixinha\n"
              "16 - Ver caixinhas\n17 - Simular rendimento\n"
              "18 - Comprar no credito\n19 - Ver fatura\n20 - Pagar fatura\n"
              "21 - Comprar moeda\n22 - Vender moeda\n23 - Ver carteira\n"
              "24 - Simular emprestimo\n25 - Contratar emprestimo\n"
              "26 - Pagar parcela\n27 - Voltar")
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
            relatorio_categoria(conta)
        elif opcao == "11":
            consultar_pontos(conta)
        elif opcao == "12":
            resgatar_cashback(conta)
        elif opcao == "13":
            criar_cofrinho(conta)
        elif opcao == "14":
            guardar_no_cofrinho(conta)
        elif opcao == "15":
            resgatar_do_cofrinho(conta)
        elif opcao == "16":
            ver_cofrinhos(conta)
        elif opcao == "17":
            simular_rendimento(conta)
        elif opcao == "18":
            comprar_no_credito(conta)
        elif opcao == "19":
            ver_fatura(conta)
        elif opcao == "20":
            pagar_fatura(conta)
        elif opcao == "21":
            comprar_moeda_estrangeira(conta)
        elif opcao == "22":
            vender_moeda_estrangeira(conta)
        elif opcao == "23":
            ver_carteira(conta)
        elif opcao == "24":
            simular_emprestimo(conta)
        elif opcao == "25":
            contratar_emprestimo(conta)
        elif opcao == "26":
            pagar_parcela_emprestimo(conta)
        elif opcao == "27":
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
