def analisar_log(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except OSError:
        print("Nao foi possivel abrir o arquivo de log.")
        return None
    sucesso = 0
    nao_encontrado = 0
    for linha in linhas:
        partes = linha.split('"')
        if len(partes) < 3:
            continue
        campos = partes[2].split()
        if not campos:
            continue
        if campos[0] == "200":
            sucesso += 1
        elif campos[0] == "404":
            nao_encontrado += 1
    return {"200": sucesso, "404": nao_encontrado}


def mostrar_analise_log():
    caminho = input("Caminho do arquivo de log: ").strip()
    resultado = analisar_log(caminho)
    if resultado is None:
        return
    print(f"Sucesso (200): {resultado['200']}")
    print(f"Nao encontrado (404): {resultado['404']}")
