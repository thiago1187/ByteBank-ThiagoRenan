from banco import buscar_por_chave, registrar
from entrada import escolher_categoria, ler_valor
from pontos import creditar_pontos, debitar_pontos

ESTORNAVEIS = ["deposito", "saque", "pix", "boleto"]


def depositar(conta):
    valor = ler_valor("Valor do deposito: R$ ")
    if valor is None:
        return
    conta["saldo"] += valor
    registrar(conta, "deposito", valor, None)
    print(f"Deposito de R$ {valor:.2f} realizado. Saldo: R$ {conta['saldo']:.2f}")


def sacar(conta):
    valor = ler_valor("Valor do saque: R$ ")
    if valor is None:
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    categoria = escolher_categoria()
    if categoria is None:
        return
    conta["saldo"] -= valor
    registrar(conta, "saque", valor, None, categoria)
    creditar_pontos(conta, valor)
    print(f"Saque de R$ {valor:.2f} em {categoria}. Saldo: R$ {conta['saldo']:.2f}")


def pix(conta):
    destino = buscar_por_chave(input("Chave pix de destino: ").strip())
    if destino is None:
        print("Chave pix nao encontrada.")
        return
    if destino is conta:
        print("Nao da para transferir para a propria conta.")
        return
    valor = ler_valor("Valor do pix: R$ ")
    if valor is None:
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    categoria = escolher_categoria()
    if categoria is None:
        return
    conta["saldo"] -= valor
    destino["saldo"] += valor
    registrar(destino, "pix_recebido", valor, conta["chave_pix"])
    registrar(conta, "pix", valor, destino["chave_pix"], categoria)
    creditar_pontos(conta, valor)
    print(f"Pix de R$ {valor:.2f} enviado para {destino['nome']}. Saldo: R$ {conta['saldo']:.2f}")


def mostrar_extrato(conta):
    if not conta["extrato"]:
        print("Nenhuma transacao registrada.")
        return
    print("Extrato (mais recente primeiro):")
    for transacao in reversed(conta["extrato"]):
        linha = f"{transacao['tipo']} - R$ {transacao['valor']:.2f}"
        if transacao["categoria"] is not None:
            linha += f" - {transacao['categoria']}"
        print(linha)


def estornar(conta):
    if not conta["extrato"]:
        print("Nao ha transacao para estornar.")
        return
    if conta["extrato"][-1]["tipo"] not in ESTORNAVEIS:
        print("A ultima transacao nao pode ser estornada.")
        return
    transacao = conta["extrato"].pop()
    tipo, valor = transacao["tipo"], transacao["valor"]
    if tipo == "pix":
        destino = buscar_por_chave(transacao["destino"])
        if destino is not None and destino["saldo"] < valor:
            print("O destino nao tem saldo para o estorno.")
            conta["extrato"].append(transacao)
            return
    if tipo == "deposito":
        conta["saldo"] -= valor
    else:
        conta["saldo"] += valor
    if tipo == "pix":
        destino = buscar_por_chave(transacao["destino"])
        if destino is not None:
            destino["saldo"] -= valor
    if tipo in ("saque", "pix"):
        debitar_pontos(conta, valor)
    print(f"Estorno de {tipo} no valor de R$ {valor:.2f}. Saldo: R$ {conta['saldo']:.2f}")
