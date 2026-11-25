# Fase 4 - Funcao de expansao

from mapa import mapa_romenia, heuristica_bucareste


# Mostrar a fronteira
def mostrar_fronteira(fronteira):
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')
    print('   fronteira:', ', '.join(partes))


# Expandir um no
def expandir(no, explorados):
    f_atual, g_atual, cidade_atual, caminho = no
    filhos = []

    for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
        if vizinho in explorados:
            continue

        novo_g = g_atual + custo_estrada
        novo_f = novo_g + heuristica_bucareste[vizinho]

        filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    return filhos


# Preparar a fronteira
inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()


# Executar tres rodadas da busca
for rodada in [1, 2, 3]:
    fronteira.sort(key=lambda no: no[0])

    no = fronteira.pop(0)
    f, g, cidade, caminho = no

    print()
    print(f'Rodada {rodada}: expandindo {cidade} (f={f})')

    explorados.add(cidade)

    filhos = expandir(no, explorados)
    fronteira = fronteira + filhos

    mostrar_fronteira(fronteira)

print()
print('Cidades exploradas:', explorados)