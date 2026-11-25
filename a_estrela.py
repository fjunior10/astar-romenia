# -*- coding: utf-8 -*-
# Fase 6 - Programa completo da busca A*
# f(n) = g(n) + h(n)
# g(n): custo real percorrido
# h(n): estimativa ate Bucareste
# f(n): custo total estimado

from mapa import mapa_romenia, heuristica_bucareste


# PASSO 2 - Funcao de apoio
def resumo_fronteira(fronteira):
    return ', '.join(f'{cidade}({f})' for f, g, cidade, caminho in fronteira)


# PASSO 3 - Algoritmo A*
def busca_a_estrela(inicio, objetivo, grafo, heuristica, mostrar=True):
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    iteracao = 0

    if mostrar:
        print(f'--- Busca A* de {inicio} para {objetivo} ---')

    while fronteira:
        iteracao = iteracao + 1
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        if mostrar:
            print(f'{iteracao}. Expandindo: {cidade_atual} | '
                  f'g(n)={g_atual}, h(n)={heuristica[cidade_atual]} '
                  f'-> f(n)={f_atual}')

        if cidade_atual == objetivo:
            return caminho, g_atual

        if cidade_atual in explorados:
            continue

        explorados.add(cidade_atual)

        for vizinho, custo_estrada in grafo.get(cidade_atual, []):
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica[vizinho]

                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print('   fronteira:', resumo_fronteira(fronteira))

    return None, float('inf')


# PASSO 4 - Programa principal
def main():
    caminho, custo = busca_a_estrela(
        'Arad', 'Bucharest', mapa_romenia, heuristica_bucareste
    )

    print()
    print('--- Resultado ---')

    if caminho:
        print('Caminho encontrado:', ' -> '.join(caminho))
        print(f'Custo real total: {custo} km em {len(caminho) - 1} passos')
    else:
        print('Não foi possível encontrar um caminho.')

    # Teste de regressao
    if caminho and custo == 418 and len(caminho) - 1 == 4:
        print('Conferido: igual ao livro (418 km, 4 passos).')
    else:
        print('ATENÇÃO: o livro espera 418 km em 4 passos. Revise o código.')

    print()
    print('--- Outras origens (sem rastro) ---')

    for origem in ['Timisoara', 'Oradea', 'Craiova', 'Iasi']:
        caminho, custo = busca_a_estrela(
            origem, 'Bucharest', mapa_romenia,
            heuristica_bucareste, mostrar=False
        )

        print(f'{origem:<10} {custo:>4} km ', ' -> '.join(caminho))


# PASSO 5 - Executar o programa principal
if __name__ == '__main__':
    main()