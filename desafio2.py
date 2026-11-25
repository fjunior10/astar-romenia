from fase2_caminhos import custo_do_caminho, mostrar_g_h_f

caminho = [
    'Arad',
    'Timisoara',
    'Lugoj',
    'Mehadia',
    'Drobeta',
    'Craiova',
    'Pitesti',
    'Bucharest'
]

# Desafio 1 - Calcular o custo
print()
print('--- Desafio 1 ---')
print('Caminho:', ' -> '.join(caminho))
print('Custo:', custo_do_caminho(caminho), 'km')

# Desafio 2 - Mostrar g, h e f
print()
print('--- Desafio 2 ---')
mostrar_g_h_f(caminho)
