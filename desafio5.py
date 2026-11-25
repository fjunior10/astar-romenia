from mapa import mapa_romenia, heuristica_bucareste

def buscar(inicio, objetivo, gulosa=False, antecipado=False):
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:

        if gulosa:
            fronteira.sort(
                key=lambda no: heuristica_bucareste[no[2]]
            )
        else:
            fronteira.sort(key=lambda no: no[0])

        f, g, cidade, caminho = fronteira.pop(0)

        if cidade == objetivo:
            return caminho, g

        if cidade in explorados:
            continue

        explorados.add(cidade)

        for vizinho, custo in mapa_romenia[cidade]:
            if vizinho not in explorados:
                novo_g = g + custo

                if antecipado and vizinho == objetivo:
                    return caminho + [vizinho], novo_g

                novo_f = novo_g + heuristica_bucareste[vizinho]

                fronteira.append(
                    (novo_f, novo_g, vizinho, caminho + [vizinho])
                )

    return None, float('inf')


# Desafio 1 - Busca gulosa
print('--- Desafio 1: Busca gulosa ---')

caminho, custo = buscar('Arad', 'Bucharest', gulosa=True)

print('Caminho:', ' -> '.join(caminho))
print('Custo:', custo, 'km')


# Desafio 2 - Teste de objetivo antecipado
print()
print('--- Desafio 2: Objetivo antecipado ---')

caminho, custo = buscar('Arad', 'Bucharest', antecipado=True)

print('Caminho:', ' -> '.join(caminho))
print('Custo:', custo, 'km')

print('O algoritmo aceita o primeiro destino encontrado')
print('sem verificar se existe um caminho mais barato.')