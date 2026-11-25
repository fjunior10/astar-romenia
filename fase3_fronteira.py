# Fase 3 - No de busca e fronteira

from mapa import mapa_romenia, heuristica_bucareste

# Montar o no inicial
inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

fronteira = [no_inicial]
print('Fronteira no começo:', fronteira)

# Retirar o primeiro no
no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no

print()
print('Nó retirado:', no)
print('f =', f_atual, '| g =', g_atual,
      '| cidade =', cidade_atual, '| caminho =', caminho)
print('Fronteira agora:', fronteira)

# Gerar os filhos do no retirado
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]

    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

print()
print('Fronteira depois de expandir Arad:')
for item in fronteira:
    print(' ', item)

# Ordenar a fronteira pelo menor f
fronteira.sort(key=lambda no: no[0])

print()
print('Fronteira ordenada pelo f:')
for item in fronteira:
    print(' ', item)

# Escolher o proximo no
proximo = fronteira.pop(0)

print()
print('Próximo nó a expandir:', proximo[2], 'com f =', proximo[0])