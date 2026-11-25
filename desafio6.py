from mapa import mapa_romenia, heuristica_bucareste

def buscar(inicio, objetivo, heuristica):
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    iteracoes = 0

    while fronteira:
        iteracoes += 1

        fronteira.sort(key=lambda no: no[0])
        f, g, cidade, caminho = fronteira.pop(0)

        if cidade == objetivo:
            return caminho, g, iteracoes

        if cidade in explorados:
            continue

        explorados.add(cidade)

        for vizinho, custo in mapa_romenia[cidade]:
            if vizinho not in explorados:
                novo_g = g + custo
                novo_f = novo_g + heuristica[vizinho]

                fronteira.append(
                    (novo_f, novo_g, vizinho, caminho + [vizinho])
                )

    return None, float('inf'), iteracoes


# Desafio 1 - Heuristica zero
print('--- Desafio 1: Heuristica zero ---')

h_zero = {c: 0 for c in mapa_romenia}

caminho, custo, iteracoes = buscar(
    'Arad', 'Bucharest', h_zero
)

print('Caminho:', ' -> '.join(caminho))
print('Custo:', custo, 'km')
print('Iteracoes:', iteracoes)


# Desafio 2 - Outras cidades
print()
print('--- Desafio 2: Outras origens ---')

for origem in ['Lugoj', 'Mehadia', 'Eforie']:
    caminho, custo, iteracoes = buscar(
        origem, 'Bucharest', heuristica_bucareste
    )

    print('Origem:', origem)
    print('Caminho:', ' -> '.join(caminho))
    print('Custo:', custo, 'km')
    print('Iteracoes:', iteracoes)
    print()


# Desafio 3 - Contagem de iteracoes
print('--- Desafio 3: Iteracoes do A* ---')

caminho, custo, iteracoes = buscar(
    'Arad', 'Bucharest', heuristica_bucareste
)

print('Custo:', custo, 'km')
print('Iteracoes:', iteracoes)