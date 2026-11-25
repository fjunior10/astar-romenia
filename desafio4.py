from mapa import mapa_romenia, heuristica_bucareste

def expandir(no, explorados):
    f_atual, g_atual, cidade_atual, caminho = no
    filhos = []

    for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
        if vizinho in explorados:
            continue

        novo_g = g_atual + custo_estrada
        novo_f = novo_g + heuristica_bucareste[vizinho]

        filhos.append(
            (novo_f, novo_g, vizinho, caminho + [vizinho])
        )

    return filhos

inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

for rodada in range(1, 7):
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)

    f, g, cidade, caminho = no

    print('Rodada', rodada, ':', cidade, 'f =', f)

    explorados.add(cidade)
    fronteira = fronteira + expandir(no, explorados)

print()
print('Falta uma condicao de parada ao chegar ao objetivo.')
