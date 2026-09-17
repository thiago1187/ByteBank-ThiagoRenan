CATEGORIAS = ["Alimentacao", "Transporte", "Lazer", "Contas", "Outros"]


def ler_valor(mensagem):
    try:
        valor = float(input(mensagem))
    except ValueError:
        print("Valor invalido.")
        return None
    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return None
    return valor


def escolher_categoria():
    print("Categorias:")
    for indice, categoria in enumerate(CATEGORIAS, 1):
        print(f"{indice} - {categoria}")
    try:
        escolha = int(input("Categoria do gasto: "))
    except ValueError:
        print("Categoria invalida.")
        return None
    if escolha < 1 or escolha > len(CATEGORIAS):
        print("Categoria invalida.")
        return None
    return CATEGORIAS[escolha - 1]
