LIMITE_CREDITO_INICIAL = 1000.0

contas = []


def buscar_por_chave(chave):
    for conta in contas:
        if conta["chave_pix"] == chave:
            return conta
    return None

def buscar_por_cpf(cpf):
    for conta in contas:
        if conta["cpf"] == cpf:
            return conta
    return None


def limpar_cpf(texto):
    return texto.replace(".", "").replace("-", "").strip()


def buscar_por_numero(numero):
    for conta in contas:
        if conta["numero"] == numero:
            return conta
    return None


def cadastrar_conta():
    nome = input("Nome do titular: ").strip()
    cpf = limpar_cpf(input("CPF (so numeros): "))
    chave_pix = input("Chave pix: ").strip()
    if not nome or not chave_pix:
        print("Nome e chave pix nao podem ficar em branco.")
        return
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF invalido. Digite os 11 numeros.")
        return
    if buscar_por_cpf(cpf) is not None:
        print("Ja existe uma conta com esse CPF.")
        return
    if buscar_por_chave(chave_pix) is not None:
        print("Ja existe uma conta com essa chave pix.")
        return
    contas.append({
        "numero": len(contas) + 1, "nome": nome, "cpf": cpf, "chave_pix": chave_pix,
        "saldo": 0.0, "extrato": [], "boletos": [], "pontos": 0, "cofrinhos": {},
        "limite_credito": LIMITE_CREDITO_INICIAL, "fatura": 0.0, "compras_credito": [],
        "moedas": {}, "parcelas": [],
    })
    print(f"Conta {len(contas)} criada para {nome}.")


def acessar_conta():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    print("Contas cadastradas:")
    for conta in contas:
        print(f"{conta['numero']} - {conta['nome']} - CPF {conta['cpf']}")
    texto = input("Numero da conta ou CPF: ").strip()
    if len(limpar_cpf(texto)) == 11:
        return buscar_por_cpf(limpar_cpf(texto))
    try:
        numero = int(texto)
    except ValueError:
        print("Numero invalido.")
        return None
    return buscar_por_numero(numero)


def mostrar_saldo(conta):
    print(f"{conta['nome']}: R$ {conta['saldo']:.2f}")


def registrar(conta, tipo, valor, destino, categoria=None):
    conta["extrato"].append({
        "tipo": tipo, "valor": valor, "destino": destino, "categoria": categoria,
    })


def resumo_conta(conta):
    guardado = sum(cofrinho["saldo"] for cofrinho in conta["cofrinhos"].values())
    return (f"Saldo: R$ {conta['saldo']:.2f} | Guardado: R$ {guardado:.2f} | "
            f"Fatura: R$ {conta['fatura']:.2f} | {conta['pontos']} BytePoints | "
            f"{len(conta['boletos'])} boleto(s) na fila")
