from banco import registrar
from entrada import escolher_categoria, ler_valor


def agendar_boleto(conta):
    descricao = input("Descricao do boleto: ").strip()
    if not descricao:
        print("A descricao nao pode ficar em branco.")
        return
    valor = ler_valor("Valor do boleto: R$ ")
    if valor is None:
        return
    categoria = escolher_categoria()
    if categoria is None:
        return
    conta["boletos"].append({"descricao": descricao, "valor": valor, "categoria": categoria})
    print(f"Boleto '{descricao}' de R$ {valor:.2f} agendado em {categoria}.")


def ver_fila(conta):
    if not conta["boletos"]:
        print("Nenhum boleto na fila.")
        return
    print("Fila de boletos (proximo a pagar primeiro):")
    for boleto in conta["boletos"]:
        print(f"{boleto['descricao']} - R$ {boleto['valor']:.2f} - {boleto['categoria']}")


def liquidar_pagamentos(conta):
    if not conta["boletos"]:
        print("Nenhum boleto na fila.")
        return
    while conta["boletos"]:
        proximo = conta["boletos"][0]
        if proximo["valor"] > conta["saldo"]:
            print(f"Sem saldo para o boleto '{proximo['descricao']}' de R$ {proximo['valor']:.2f}.")
            break
        conta["boletos"].pop(0)
        conta["saldo"] -= proximo["valor"]
        registrar(conta, "boleto", proximo["valor"], None, proximo["categoria"])
        print(f"Boleto '{proximo['descricao']}' pago. Saldo: R$ {conta['saldo']:.2f}")
