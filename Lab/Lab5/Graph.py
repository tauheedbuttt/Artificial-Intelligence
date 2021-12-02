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

    def dfs(self, start, goal):
        visited = []
        self.df_s((start,0), goal, visited)
        return ([node[0] for node in visited], sum([node[1] for node in visited]))

    def df_s(self, node, goal, visited):
        visited.append(node)
        if node[0] == goal:
            return True
        for child in self.adj_list[node[0]]:
            if child in visited:
                continue
            stop = self.df_s(child, goal, visited)
            if stop:
                return stop
        return False
    
    def dls(self, start, goal, limit):
        if not limit:
            return ([], 0)
        visited = []
        self.dl_s((start,0), goal, limit, visited)
        return ([node[0] for node in visited], sum([node[1] for node in visited]))

    def dl_s(self, node, goal, limit, visited):
        if limit == 0:
            return True
        visited.append(node)
        if node == goal:
            return True
        for child in self.adj_list[node[0]]:
            if child in visited:
                continue
            stop = self.dl_s(child, goal, limit-1, visited)
            if stop:
                return stop
        return False
    
    def iddls(self, start, goal):
        limit = 1
        while True:
            path = self.dls(start, goal, limit)
            if goal in path[0]:
                return path
            limit += 1

