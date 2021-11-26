from Graph import *
from PriorityQueue import *


def find_path(g, start, end, cost=0, path=[]):
    path.append(start)
    if start == end:
        return path,cost
    if start not in g.nodes:
        return None
    for node in g.adj_list[start]:
        cost += node[1]
        newpath,cost = find_path(g, node[0], end, cost, path)
        if newpath:
            return newpath,cost
    return None



nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B', 2), ('A', 'C', 1), ('B', 'C', 2), ('B', 'D', 5), ('C', 'D', 1), ('C', 'F', 3), 
    ('D', 'C', 1), ('D', 'E', 4), ('E', 'F', 3), ('F', 'C', 1), ('F', 'E', 2)    
]

g = Graph(nodes, True)

for src,dst,cost in edges:
    g.add_edge(src, dst, cost)

print(g)
path,cost = find_path(g, 'A', 'D')
print(f'Path: {path}\nCost: {cost}')