from banco import registrar
from entrada import ler_valor

JUROS_POR_PARCELA = 0.02
MAXIMO_DE_PARCELAS = 24


def limite_de_emprestimo(conta):
    return conta["saldo"] * 3


def simular_emprestimo(conta):
    limite = limite_de_emprestimo(conta)
    print(f"Limite pre-aprovado: R$ {limite:.2f}")
    valor = ler_valor("Valor do emprestimo: R$ ")
    if valor is None:
        return None
    if valor > limite:
        print("Valor acima do limite pre-aprovado.")
        return None
    try:
        parcelas = int(input("Em quantas parcelas: "))
    except ValueError:
        print("Numero de parcelas invalido.")
        return None
    if parcelas < 1 or parcelas > MAXIMO_DE_PARCELAS:
        print(f"O parcelamento vai de 1 a {MAXIMO_DE_PARCELAS} parcelas.")
        return None
    total = valor * (1 + JUROS_POR_PARCELA * parcelas)
    print(f"{parcelas}x de R$ {total / parcelas:.2f}, total de R$ {total:.2f}")
    return valor, parcelas, total


def contratar_emprestimo(conta):
    if conta["parcelas"]:
        print("Ja existe um emprestimo em andamento.")
        return
    simulacao = simular_emprestimo(conta)
    if simulacao is None:
        return
    valor, parcelas, total = simulacao
    if input("Confirma a contratacao (s/n): ").strip().lower() != "s":
        print("Contratacao cancelada.")
        return
    conta["saldo"] += valor
    conta["parcelas"] = [total / parcelas] * parcelas
    registrar(conta, "emprestimo", valor, None)
    print(f"Emprestimo de R$ {valor:.2f} creditado em {parcelas}x. Saldo: R$ {conta['saldo']:.2f}")


def pagar_parcela_emprestimo(conta):
    if not conta["parcelas"]:
        print("Nao ha parcela a pagar.")
        return
    parcela = conta["parcelas"][0]
    if parcela > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    conta["parcelas"].pop(0)
    conta["saldo"] -= parcela
    registrar(conta, "parcela", parcela, None)
    print(f"Parcela de R$ {parcela:.2f} paga. Faltam {len(conta['parcelas'])} parcelas. "
          f"Saldo: R$ {conta['saldo']:.2f}")
