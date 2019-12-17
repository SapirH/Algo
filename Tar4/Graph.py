# Written by:
# Sapir Holzman 318265097
# Shahaf Shavit 314967324

class Graph:
    def __init__(self):
        self.vertices = {}

    def __getitem__(self, key):
        return self.vertices[key]

    def keys(self):
        return self.vertices.keys()

    def add_vertex(self, vertex):
        self.vertices[vertex.id] = vertex

    def add_edge(self, u, v, w):
        u.add_adj(v, w)


class Vertex:
    def __init__(self, _id, weight=None):
        self.id = _id
        self.adjacent = []
        if weight != None:
            self.weight = weight


    def add_adj(self, vertex_adj, w=0):
        new_adj={ "id": vertex_adj.id, "weight": w }
        self.adjacent.append(new_adj)

    def get_adj_weight(self, curr_adj):
        for adj in self.adjacent:
            if adj["id"] == curr_adj.id:
                return adj["weight"]

    def __str__(self):
        return '{} and adj {}'.format(self.id, self.adjacent)


class AStarGraphVertex(Vertex):
    def __init__(self, _id):
        super().__init__(_id)
        self.h = 0
        self.g = 0
