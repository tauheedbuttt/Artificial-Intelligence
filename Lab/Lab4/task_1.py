from Graph import *
from PriorityQueue import *


def shortest_path(g, start, end, path=[]):
    path.append(start)
    if start == end:
        return path
    if start not in g.nodes:
        return None
    q = PriorityQueue(g.adj_list[start])
    while not q.is_empty():
        node = q.pop()
        newpath = shortest_path(g, node[0], end, path)
        if newpath:
            return newpath
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
print(shortest_path(g, 'A', 'D'))