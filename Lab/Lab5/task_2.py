from Graph import Graph

nodes = ['S', 'A', 'B', 'C']

edges = [
    ('S', 'A', 5),
    ('S', 'B', 5),
    ('S', 'C', 1),
]

g = Graph(nodes, True)

for src, dst, cost in edges:
    g.add_edge(src, dst, cost)

print('(Path, Cost)')
print(f"DFS: {g.dfs('S', 'C')}")
print(f"IDDFS: {g.iddls('S', 'C')}")