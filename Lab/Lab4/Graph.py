class Graph:
    def __init__(self, nodes, is_directed=False):
        self.nodes = nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def __str__(self):
        string = ""
        for node in self.nodes:
            string += f"{node} -> {self.adj_list[node]}\n"
        return string

    def create_directed_edge(self, src, dst, cost):
        if dst in self.nodes:
            self.adj_list[src].append((dst, cost))


    def create_undirected_edge(self, src, dst):
        if (dst not in self.nodes) or (src not in self.nodes) or (len(dst) > 1) or (len(src) > 1):
            return
        self.adj_list[src].append(dst, cost)
        self.adj_list[dst].append(src, cost)

    def add_edge(self, src, dst, cost):
        if self.is_directed:
            self.create_directed_edge(src, dst, cost)
        else:
            self.create_undirected_edge(src, dst, cost)