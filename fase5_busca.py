# Fase 5 - Busca A* com laco while

from mapa import mapa_romenia, heuristica_bucareste


def busca_a_estrela(inicio, objetivo):
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:

        # Escolher o no de menor f
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        # Verificar se chegou ao objetivo
        if cidade_atual == objetivo:
            return caminho, g_atual

        # Ignorar cidades ja exploradas
        if cidade_atual in explorados:
            continue

        explorados.add(cidade_atual)

        # Gerar os filhos
        for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica_bucareste[vizinho]

                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf')


# Executar a busca
caminho, custo = busca_a_estrela('Arad', 'Bucharest')

print('Caminho:', ' -> '.join(caminho))
print('Custo :', custo, 'km')
print('Passos :', len(caminho) - 1, 'estradas')