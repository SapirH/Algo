# Written by:
# Sapir Holzman 318265097
# Shahaf Shavit 314967324


class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex(self, _id):
        return self.vertices[_id]

    @property
    def vertices_ids(self):
        return self.vertices.keys()

    def add_vertex(self, vertex):
        self.vertices[vertex.id] = vertex

    def add_edge(self, u, v, w):
        u.add_adj(v, w)


class Vertex:
    def __init__(self, _id):
        self.id = _id
        self.adjacent = []

    def add_adj(self, vertex_adj, w=0):
        new_adj = {'id': vertex_adj.id, 'weight': w}
        self.adjacent.append(new_adj)

    def get_adj_weight(self, curr_adj):
        for adj in self.adjacent:
            if adj['id'] == curr_adj.id:
                return adj['weight']
        raise Exception('Adjacent vertex wasn\'t found.')

    def __str__(self):
        return '{} and adj {}'.format(self.id, self.adjacent)


class AStarGraphVertex(Vertex):
    def __init__(self, _id, heuristic_weight):
        super().__init__(_id)
        self.heuristic_weight = heuristic_weight
        self.g = 0
