from banco import registrar
from entrada import escolher_categoria, ler_valor


def comprar_no_credito(conta):
    disponivel = conta["limite_credito"] - conta["fatura"]
    print(f"Limite disponivel: R$ {disponivel:.2f}")
    estabelecimento = input("Estabelecimento: ").strip()
    if not estabelecimento:
        print("O estabelecimento nao pode ficar em branco.")
        return
    valor = ler_valor("Valor da compra: R$ ")
    if valor is None:
        return
    if valor > disponivel:
        print("Limite insuficiente.")
        return
    categoria = escolher_categoria()
    if categoria is None:
        return
    conta["fatura"] += valor
    conta["compras_credito"].append({
        "estabelecimento": estabelecimento, "valor": valor, "categoria": categoria,
    })
    registrar(conta, "credito", valor, estabelecimento, categoria)
    print(f"Compra de R$ {valor:.2f} em {estabelecimento}. Fatura: R$ {conta['fatura']:.2f}")


def ver_fatura(conta):
    for compra in conta["compras_credito"]:
        print(f"{compra['estabelecimento']} - R$ {compra['valor']:.2f} - {compra['categoria']}")
    print(f"Fatura: R$ {conta['fatura']:.2f}")
    print(f"Limite disponivel: R$ {conta['limite_credito'] - conta['fatura']:.2f}")


def pagar_fatura(conta):
    if conta["fatura"] <= 0:
        print("Nao ha fatura em aberto.")
        return
    if conta["fatura"] > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    valor = conta["fatura"]
    conta["saldo"] -= valor
    conta["fatura"] = 0.0
    conta["compras_credito"] = []
    registrar(conta, "fatura", valor, None)
    print(f"Fatura de R$ {valor:.2f} paga. Saldo: R$ {conta['saldo']:.2f}")
