from banco import registrar
from entrada import ler_valor

RENDIMENTO_MENSAL = 0.005


def criar_cofrinho(conta):
    nome = input("Nome da caixinha: ").strip()
    if not nome:
        print("O nome nao pode ficar em branco.")
        return
    if nome in conta["cofrinhos"]:
        print("Ja existe uma caixinha com esse nome.")
        return
    objetivo = ler_valor("Objetivo de quanto quer guardar: R$ ")
    if objetivo is None:
        return
    conta["cofrinhos"][nome] = {"objetivo": objetivo, "saldo": 0.0}
    print(f"Caixinha '{nome}' criada com objetivo de R$ {objetivo:.2f}.")


def guardar_no_cofrinho(conta):
    nome = input("Nome da caixinha: ").strip()
    if nome not in conta["cofrinhos"]:
        print("Caixinha nao encontrada.")
        return
    valor = ler_valor("Quanto quer guardar: R$ ")
    if valor is None:
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    conta["saldo"] -= valor
    conta["cofrinhos"][nome]["saldo"] += valor
    registrar(conta, "cofrinho", valor, nome)
    print(f"R$ {valor:.2f} guardados em '{nome}'. Saldo: R$ {conta['saldo']:.2f}")


def resgatar_do_cofrinho(conta):
    nome = input("Nome da caixinha: ").strip()
    if nome not in conta["cofrinhos"]:
        print("Caixinha nao encontrada.")
        return
    valor = ler_valor("Quanto quer resgatar: R$ ")
    if valor is None:
        return
    if valor > conta["cofrinhos"][nome]["saldo"]:
        print("A caixinha nao tem esse valor.")
        return
    conta["cofrinhos"][nome]["saldo"] -= valor
    conta["saldo"] += valor
    registrar(conta, "resgate", valor, nome)
    print(f"R$ {valor:.2f} resgatados de '{nome}'. Saldo: R$ {conta['saldo']:.2f}")


def ver_cofrinhos(conta):
    if not conta["cofrinhos"]:
        print("Nenhuma caixinha criada.")
        return
    print("Caixinhas:")
    for nome, cofrinho in conta["cofrinhos"].items():
        print(f"{nome} - R$ {cofrinho['saldo']:.2f} de R$ {cofrinho['objetivo']:.2f}")


def simular_rendimento(conta):
    if not conta["cofrinhos"]:
        print("Nenhuma caixinha criada.")
        return
    for nome, cofrinho in conta["cofrinhos"].items():
        juros = cofrinho["saldo"] * RENDIMENTO_MENSAL
        cofrinho["saldo"] += juros
        print(f"{nome} - rendimento de R$ {juros:.2f}, saldo R$ {cofrinho['saldo']:.2f}")
