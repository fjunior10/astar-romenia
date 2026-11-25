# Fase 1 - Explorar os dados do mapa

from mapa import mapa_romenia, heuristica_bucareste

# Quantidade de cidades
print('Quantidade de cidades no mapa:', len(mapa_romenia))
print('Quantidade de valores de h(n):', len(heuristica_bucareste))

# Vizinhos de Arad
vizinhos_arad = mapa_romenia['Arad']
print()
print('Vizinhos de Arad:', vizinhos_arad)
print('Tipo do valor:', type(vizinhos_arad))

# Primeira estrada
primeira = vizinhos_arad[0]
print()
print('Primeira estrada que sai de Arad:', primeira)
print('Cidade vizinha:', primeira[0])
print('Custo em km:', primeira[1])

# Percorrer as estradas de Arad
print()
print('Estradas que saem de Arad:')
for vizinho, custo in mapa_romenia['Arad']:
    print('Arad ->', vizinho, '=', custo, 'km')

# Percorrer o mapa inteiro
print()
print('Número de estradas de cada cidade:')
for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    print(f'{cidade:<15} {quantidade} estrada(s)')

# Consultar a heurística
print()
print('h(Arad) =', heuristica_bucareste['Arad'], 'km')

for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f'{vizinho:<10} estrada = {custo:>3} km    h = {h:>3} km')