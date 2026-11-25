from mapa import mapa_romenia, heuristica_bucareste

# Desafio 1 - Expandir Sibiu

fronteira = [
    (447, 118, 'Timisoara', ['Arad', 'Timisoara']),
    (449, 75, 'Zerind', ['Arad', 'Zerind'])
]

g_atual = 140
cidade_atual = 'Sibiu'
caminho = ['Arad', 'Sibiu']

for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]

    fronteira.append(
        (novo_f, novo_g, vizinho, novo_caminho)
    )

fronteira.sort(key=lambda no: no[0])

print('--- Desafio 1 ---')

for f, g, cidade, caminho in fronteira:
    print(cidade, 'f =', f)

print('Arad apareceu porque ainda nao filtramos cidades exploradas.')

# Desafio 2 - Ordenar pelo custo g

fronteira.sort(key=lambda no: no[1])

print()
print('--- Desafio 2 ---')

for f, g, cidade, caminho in fronteira:
    print(cidade, 'g =', g)

proximo = fronteira.pop(0)

print('Primeiro no:', proximo[2])
print('Custo g:', proximo[1], 'km')
