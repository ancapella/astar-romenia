mapa_romenia = {
    'Arad':           [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind':         [('Arad', 75), ('Oradea', 71)],
    'Oradea':         [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu':          [('Arad', 140), ('Oradea', 151), ('Fagaras', 99),
                       ('Rimnicu Vilcea', 80)],
    'Timisoara':      [('Arad', 118), ('Lugoj', 111)],
    'Lugoj':          [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia':        [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta':        [('Mehadia', 75), ('Craiova', 120)],
    'Craiova':        [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras':        [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti':        [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest':      [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90),
                       ('Urziceni', 85)],
    'Giurgiu':        [('Bucharest', 90)],
    'Urziceni':       [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova':        [('Urziceni', 98), ('Eforie', 86)],
    'Eforie':         [('Hirsova', 86)],
    'Vaslui':         [('Urziceni', 142), ('Iasi', 92)],
    'Iasi':           [('Vaslui', 92), ('Neamt', 87)],
    'Neamt':          [('Iasi', 87)],
}

from mapa import mapa_romenia, heuristica_bucareste

print('Quantidade de cidades no mapa:', len(mapa_romenia))
print('Quantidade de valores de h(n):', len(heuristica_bucareste))

vizinhos_arad = mapa_romenia['Arad']
print()
print('Vizinhos de Arad:', vizinhos_arad)
print('Tipo do valor:', type(vizinhos_arad))

primeira = vizinhos_arad[0]
print()
print('Primeira estrada que sai de Arad:', primeira)
print('  posição [0] -> cidade vizinha:', primeira[0])
print('  posição [1] -> custo em km   :', primeira[1])

print()
print('Estradas que saem de Arad:')
for vizinho, custo in mapa_romenia['Arad']:
    print('  Arad ->', vizinho, '=', custo, 'km')
