from banco import registrar

REAIS_POR_PONTO = 10.0
VALOR_DO_PONTO = 0.05


def creditar_pontos(conta, valor):
    conta["pontos"] += int(valor // REAIS_POR_PONTO)


def debitar_pontos(conta, valor):
    conta["pontos"] -= int(valor // REAIS_POR_PONTO)
    if conta["pontos"] < 0:
        conta["pontos"] = 0


def consultar_pontos(conta):
    valor = conta["pontos"] * VALOR_DO_PONTO
    print(f"Voce tem {conta['pontos']} BytePoints (R$ {valor:.2f} de cashback).")


def resgatar_cashback(conta):
    try:
        pontos = int(input("Quantos pontos quer resgatar: "))
    except ValueError:
        print("Quantidade invalida.")
        return
    if pontos < 100 or pontos % 100 != 0:
        print("O resgate precisa ser em multiplos de 100 pontos.")
        return
    if pontos > conta["pontos"]:
        print("Voce nao tem essa quantidade de pontos.")
        return
    valor = pontos * VALOR_DO_PONTO
    conta["pontos"] -= pontos
    conta["saldo"] += valor
    registrar(conta, "cashback", valor, None)
    print(f"Cashback de R$ {valor:.2f} creditado. Saldo: R$ {conta['saldo']:.2f}")
