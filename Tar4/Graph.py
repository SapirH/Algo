# Written by:
# Sapir Holzman 318265097
# Shahaf Shavit 314967324

class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, u, v, w):
        u.add_adj(v, w)


class Vertex:
    def __init__(self, _id):
        self.id = _id
        self.adjacent = []

    def add_adj(self, vertex_adj, w=0):
        vertex_adj.w=w
        self.adjacent.append(vertex_adj)

    def get_adj_weight(self, v):
        for adj in self.adjacent:
            if adj.id == v.id:
                return adj.w

    def __str__(self):
        return '{} and adj {}'.format(self.id, self.adjacent)


class AStarGraphVertex(Vertex):
    def __init__(self, _id):
        super().__init__(_id)
        self.h = 0
        self.g = 0
