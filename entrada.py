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
