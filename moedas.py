from banco import registrar
from entrada import ler_valor

TAXAS = {"USD": 5.50, "EUR": 6.00, "BTC": 350000.0}


def escolher_moeda():
    print("Moedas:")
    for moeda, taxa in TAXAS.items():
        print(f"{moeda} - R$ {taxa:.2f}")
    moeda = input("Moeda: ").strip().upper()
    if moeda not in TAXAS:
        print("Moeda nao encontrada.")
        return None
    return moeda


def comprar_moeda_estrangeira(conta):
    moeda = escolher_moeda()
    if moeda is None:
        return
    valor = ler_valor("Quanto em reais quer converter: R$ ")
    if valor is None:
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    quantidade = valor / TAXAS[moeda]
    conta["saldo"] -= valor
    conta["moedas"][moeda] = conta["moedas"].get(moeda, 0.0) + quantidade
    registrar(conta, "compra_moeda", valor, moeda)
    print(f"{quantidade:.6f} {moeda} comprados por R$ {valor:.2f}. Saldo: R$ {conta['saldo']:.2f}")


def vender_moeda_estrangeira(conta):
    moeda = escolher_moeda()
    if moeda is None:
        return
    quantidade = ler_valor(f"Quanto de {moeda} quer vender: ")
    if quantidade is None:
        return
    if quantidade > conta["moedas"].get(moeda, 0.0):
        print("Voce nao tem essa quantidade.")
        return
    valor = quantidade * TAXAS[moeda]
    conta["moedas"][moeda] -= quantidade
    conta["saldo"] += valor
    registrar(conta, "venda_moeda", valor, moeda)
    print(f"{quantidade:.6f} {moeda} vendidos por R$ {valor:.2f}. Saldo: R$ {conta['saldo']:.2f}")


def ver_carteira(conta):
    if not conta["moedas"]:
        print("Nenhuma moeda comprada.")
        return
    print("Carteira:")
    for moeda, quantidade in conta["moedas"].items():
        print(f"{moeda} - {quantidade:.6f} (R$ {quantidade * TAXAS[moeda]:.2f})")
