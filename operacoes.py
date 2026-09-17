from banco import buscar_por_chave, registrar
from entrada import ler_valor


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
    conta["saldo"] -= valor
    registrar(conta, "saque", valor, None)
    print(f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {conta['saldo']:.2f}")


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
    conta["saldo"] -= valor
    destino["saldo"] += valor
    registrar(conta, "pix", valor, destino["chave_pix"])
    print(f"Pix de R$ {valor:.2f} enviado para {destino['nome']}. Saldo: R$ {conta['saldo']:.2f}")


def mostrar_extrato(conta):
    if not conta["extrato"]:
        print("Nenhuma transacao registrada.")
        return
    print("Extrato (mais recente primeiro):")
    for transacao in reversed(conta["extrato"]):
        print(f"{transacao['tipo']} - R$ {transacao['valor']:.2f}")


def estornar(conta):
    if not conta["extrato"]:
        print("Nao ha transacao para estornar.")
        return
    transacao = conta["extrato"].pop()
    tipo, valor = transacao["tipo"], transacao["valor"]
    if tipo == "deposito":
        conta["saldo"] -= valor
    else:
        conta["saldo"] += valor
    if tipo == "pix":
        destino = buscar_por_chave(transacao["destino"])
        if destino is not None:
            destino["saldo"] -= valor
    print(f"Estorno de {tipo} no valor de R$ {valor:.2f}. Saldo: R$ {conta['saldo']:.2f}")
