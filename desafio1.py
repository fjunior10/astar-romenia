from mapa import mapa_romenia, heuristica_bucareste

# Desafio 1 - Cidades com apenas uma estrada
print('Cidades com apenas uma estrada:')

for cidade in mapa_romenia:
    if len(mapa_romenia[cidade]) == 1:
        print(cidade)

# Desafio 2 - Heuristica menor que 200 km
print()
print('Cidades com h(n) menor que 200 km:')

for cidade in heuristica_bucareste:
    if heuristica_bucareste[cidade] < 200:
        print(cidade, heuristica_bucareste[cidade], 'km')

# Desafio 3 - Maior estrada do mapa
maior = 0
origem = ''
destino = ''

for cidade in mapa_romenia:
    for vizinho, custo in mapa_romenia[cidade]:
        if custo > maior:
            maior = custo
            origem = cidade
            destino = vizinho

print()
print('Maior estrada do mapa:')
print(origem, '->', destino, '=', maior, 'km')