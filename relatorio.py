def relatorio_categoria(conta):
    totais = {}
    for transacao in conta["extrato"]:
        categoria = transacao["categoria"]
        if categoria is None:
            continue
        totais[categoria] = totais.get(categoria, 0.0) + transacao["valor"]
    if not totais:
        print("Nenhum gasto com categoria registrado.")
        return
    total = sum(totais.values())
    print("Gastos por categoria:")
    for categoria, valor in totais.items():
        print(f"{categoria} - R$ {valor:.2f} ({valor / total * 100:.1f}%)")
    print(f"Total gasto: R$ {total:.2f}")
