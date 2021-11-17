from queue import LifoQueue
class Node:
    def __init__(self, data, hn):
        self.data = data
        self.hn = hn

    def __str__(self):
        return f"({self.data}: {self.hn})"

    def __repr__(self):
        return f"({self.data}: {self.hn})"

class Graph:
    def __init__(self, nodes, is_directed=False):
        self.nodes = nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node.data] = []

    def __str__(self):
        string = ""
        for node in self.nodes:
            string += f"{node.data} -> {self.adj_list[node.data]}\n"
        return string

    def create_directed_edge(self, src, dst):
        for node in self.nodes:
            if dst == node.data:
                self.adj_list[src].append(node)


    def create_undirected_edge(self, src, dst):
        if (dst not in self.nodes) or (src not in self.nodes) or (len(dst) > 1) or (len(src) > 1):
            return
        self.adj_list[src].append(dst)
        self.adj_list[dst].append(src)

    def add_edge(self, src, dst):
        if self.is_directed:
            self.create_directed_edge(src, dst)
        else:
            self.create_undirected_edge(src, dst)

    def dfs(self, goal):
        checked = [False for node in self.nodes]
        dfs = []
        self.df_s('A', goal, checked, dfs)
        return dfs

    def df_s(self, node, goal, checked, dfs):
        dfs.append(node)
        nodes = self.adj_list[node]
        if len(nodes) == 0:
            return dfs
        for n in nodes:
            node = n
            if node.data == goal:
                dfs.append(node.data)
                raise ValueError(f'DFS: {dfs}')
            index = self.nodes.index(n)
            if not checked[index]:
                checked[index] = True
                self.df_s(n.data, goal, checked, dfs)
        return dfs

nodes = [
    Node('A', 6), Node('B', 7), Node('C', 9), Node('D', 7), Node('E', 5), Node('F', 3), Node('G', 1), Node('H', 4),
    Node('I', 9), Node('J', 6), Node('K', 3), Node('L', 7), Node('M', 1), Node('N', 2), Node('O', 1), Node('P', 5),
    Node('Q', 4), Node('R', 5), Node('S', 0), Node('T', 8), Node('U', 7), Node('V', 7), Node('W', 2), Node('X', 1),
    Node('Y', 5), Node('Z', 6), Node('AA', 2), Node('AB', 8), Node('AC', 2), Node('AD', 5), Node('AE', 7),
    Node('AF', 3), Node('AG', 3), Node('AH', 5), Node('AI', 7), Node('AJ', 8), Node('AK', 4), Node('AL', 7),
    Node('AM', 5), Node('AN', 8), Node('AO', 1), Node('AP', 9), Node('AQ', 1), Node('AR', 7), Node('AS', 1),
    Node('AT', 9), Node('AU', 7), Node('AV', 1), Node('AW', 4), Node('AX', 5), Node('AY', 3)
]

edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'F'), ('C', 'G'), ('C', 'H'),
    ('D', 'I'), ('F', 'E'), ('F', 'J'), ('H', 'K'),
    ('I', 'M'), ('I', 'L'), ('J', 'N'), ('K', 'O'),
    ('L', 'Q'), ('L', 'R'), ('M', 'S'), ('N', 'T'), ('N', 'U'), ('O', 'P'), ('O', 'V'),
    ('T', 'W'), ('U', 'X'), ('V', 'AA'),
    ('W', 'AD'), ('W', 'AE'), ('X', 'Y'), ('X', 'AF'), ('AA', 'Z'), ('AA', 'AB'),
    ('AE', 'AJ'), ('AF', 'AK'), ('Z', 'AG'), ('AB', 'AC'),
    ('AJ', 'AO'), ('AK', 'AP'), ('AG', 'AL'), ('AG', 'AM'), ('AC', 'AH'), ('AC', 'AI'),
    ('AP', 'AQ'), ('AL', 'AR'), ('AI', 'AN'),
    ('AR', 'AT'), ('AN', 'AS'),
    ('AT', 'AU'), ('AT', 'AV'),
    ('AU', 'AW'), ('AU', 'AX'), ('AV', 'AY'),
]

directed = Graph(nodes, True)

for src, dest in edges:
    directed.add_edge(src, dest)

print(f"----------------DIRECTED------------------\n{directed}")

try:
    print(directed.dfs('S'))
except ValueError as e:
    print(e)


