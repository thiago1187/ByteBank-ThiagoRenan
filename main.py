from banco import acessar_conta, cadastrar_conta, mostrar_saldo, resumo_conta
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

MENU_CONTA = [
    ("Conta e movimentacoes", [
        ("1", "Consultar saldo"),
        ("2", "Depositar"),
        ("3", "Sacar"),
        ("4", "Pix"),
        ("5", "Ver extrato"),
        ("6", "Estornar ultima transacao"),
    ]),
    ("Boletos agendados", [
        ("7", "Agendar boleto"),
        ("8", "Ver fila de boletos"),
        ("9", "Liquidar pagamentos"),
    ]),
    ("Gastos e recompensas", [
        ("10", "Relatorio por categoria"),
        ("11", "Consultar pontos"),
        ("12", "Resgatar cashback"),
    ]),
    ("Caixinhas de objetivo", [
        ("13", "Criar caixinha"),
        ("14", "Guardar na caixinha"),
        ("15", "Resgatar da caixinha"),
        ("16", "Ver caixinhas"),
        ("17", "Simular rendimento"),
    ]),
    ("Cartao de credito", [
        ("18", "Comprar no credito"),
        ("19", "Ver fatura"),
        ("20", "Pagar fatura"),
    ]),
    ("Carteira de moedas", [
        ("21", "Comprar moeda"),
        ("22", "Vender moeda"),
        ("23", "Ver carteira"),
    ]),
    ("Emprestimos", [
        ("24", "Simular emprestimo"),
        ("25", "Contratar emprestimo"),
        ("26", "Pagar parcela"),
    ]),
    ("Sair", [
        ("27", "Voltar"),
    ]),
]

ACOES_CONTA = {
    "1": mostrar_saldo, "2": depositar, "3": sacar, "4": pix,
    "5": mostrar_extrato, "6": estornar, "7": agendar_boleto, "8": ver_fila,
    "9": liquidar_pagamentos, "10": relatorio_categoria, "11": consultar_pontos,
    "12": resgatar_cashback, "13": criar_cofrinho, "14": guardar_no_cofrinho,
    "15": resgatar_do_cofrinho, "16": ver_cofrinhos, "17": simular_rendimento,
    "18": comprar_no_credito, "19": ver_fatura, "20": pagar_fatura,
    "21": comprar_moeda_estrangeira, "22": vender_moeda_estrangeira,
    "23": ver_carteira, "24": simular_emprestimo, "25": contratar_emprestimo,
    "26": pagar_parcela_emprestimo,
}

MENU_INICIAL = [
    ("1", "Cadastrar conta"),
    ("2", "Acessar conta"),
    ("3", "Sair"),
]


def imprimir_opcoes(opcoes):
    for numero, titulo in opcoes:
        print(f"  {numero:>2} - {titulo}")


def menu_conta(conta):
    while True:
        print(f"\n=== Conta {conta['numero']} - {conta['nome']} ===")
        print(resumo_conta(conta))
        for secao, opcoes in MENU_CONTA:
            print(f"\n[ {secao} ]")
            imprimir_opcoes(opcoes)
        opcao = input("\nEscolha uma opcao (1 a 27): ").strip()
        if opcao == "27":
            break
        acao = ACOES_CONTA.get(opcao)
        if acao is None:
            print("Opcao invalida. Digite um numero de 1 a 27.")
        else:
            acao(conta)


def menu_inicial():
    while True:
        print("\n=== ByteBank ===")
        imprimir_opcoes(MENU_INICIAL)
        opcao = input("\nEscolha uma opcao (1 a 3): ").strip()
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
            print("Opcao invalida. Digite um numero de 1 a 3.")


menu_inicial()
