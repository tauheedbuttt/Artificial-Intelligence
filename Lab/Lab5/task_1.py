from Graph import Graph

nodes = [
    'Q', 'R', 'S', 'T',
    'M', 'N', 'O', 'P',
    'I', 'J', 'K', 'L',
    'E', 'F', 'G', 'H',
    'A', 'B', 'C', 'D'
]

edges = [
    ('A', 'E'), ('A', 'B'), 
    ('B', 'F'), ('B', 'A'),
    ('C', 'D'), ('C', 'G'),
    ('D', 'C'),
    ('E', 'I'), ('E', 'A'), 
    ('F', 'J'), ('F', 'G'), ('F', 'B'),
    ('G', 'C'), ('G', 'F'), ('G', 'H'), ('G', 'K'),
    ('H', 'G'),
    ('I', 'M'), ('I', 'E'),
    ('J', 'N'), ('J', 'K'), ('J', 'F'),
    ('K', 'O'), ('K', 'L'), ('K', 'J'), ('K', 'G'),
    ('L', 'K'),
    ('M', 'Q'), ('M', 'N'), ('M', 'I'),
    ('N', 'R'), ('N', 'O'), ('N', 'J'), ('N', 'M'),
    ('O', 'P'), ('O', 'S'), ('O', 'N'), ('O', 'K'),
    ('Q', 'M'),
    ('P', 'T'), ('P', 'O'),
    ('R', 'S'), ('R', 'N'),
    ('S', 'O'), ('S', 'R'),
    ('T', 'P')
]

g = Graph(nodes, True)

for src, dst in edges:
    g.add_edge(src, dst, 0)

print(f"DFS: {g.dfs('A', 'T')}")