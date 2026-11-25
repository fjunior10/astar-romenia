# Busca A* - Mapa da Romênia

## Sobre o projeto

Implementação do algoritmo de busca A* em Python,
para encontrar o caminho de menor custo entre Arad
e Bucareste, baseado no livro de Russell & Norvig,
capítulo 3.

**Aluno:** Fábio Manoel do Nascimento Junior

**Instituição:** FATEC Araraquara

**Disciplina:** Engenharia de Software

## Como rodar

Execute no terminal:

```bash
python a_estrela.py
```

## Resultado

Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest

- Distância total: 418 km
- Estradas percorridas: 4
- Iterações: 6
- Resultado igual à Figura 3.24 do livro.

## Algoritmo A*

O algoritmo utiliza a função:

f(n) = g(n) + h(n)

- g(n): custo real percorrido.
- h(n): estimativa da distância até o destino.
- f(n): custo total estimado.

## Fases do projeto

| Arquivo | Conteúdo |
|---|---|
| mapa.py | Mapa e heurística |
| fase1_explorar.py | Navegar nos dados |
| fase2_caminhos.py | Custo dos caminhos |
| fase3_fronteira.py | Nó e fronteira |
| fase4_expandir.py | Função de expansão |
| fase5_busca.py | Laço da busca A* |
| a_estrela.py | Programa completo |

## Tecnologias utilizadas

- Python
- Git
- GitHub
- Visual Studio Code

## Referência

Russell & Norvig - Inteligência Artificial,
Capítulo 3.
