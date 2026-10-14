import json
import os

ARQUIVO_CONTAS = "contas.txt"


def salvar_contas_txt(contas):
    with open(ARQUIVO_CONTAS, "w", encoding="utf-8") as arquivo:
        arquivo.write(json.dumps(contas, ensure_ascii=False, indent=2))


def carregar_contas_txt():
    if not os.path.exists(ARQUIVO_CONTAS):
        return []
    try:
        with open(ARQUIVO_CONTAS, "r", encoding="utf-8") as arquivo:
            return json.loads(arquivo.read())
    except (json.JSONDecodeError, OSError):
        print("Nao foi possivel ler o arquivo de contas, iniciando vazio.")
        return []
