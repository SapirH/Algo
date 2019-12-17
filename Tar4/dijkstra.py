import sys
import copy

from Graph import Graph, Vertex 

def dijkstra(graph, s):
    distance_for_adj, pi = initialize_single_source(graph, s)
    S = Graph()
    q = copy.deepcopy(graph.vertices)

    while len(q) > 0:
        u = extract_min(q, distance_for_adj)
        S.add_vertex(u)
        for v in u.adjacent:
            relax(u, graph[v["id"]], distance_for_adj, pi)

    print_dijkstra_output(graph, s, pi, distance_for_adj)


def initialize_single_source(graph, s):
    distance_for_adj = { v: sys.maxsize for v in graph.keys()}
    distance_for_adj[s.id] = 0

    pi = {v: None for v in graph.keys()}

    return distance_for_adj, pi


def extract_min(q, distance_for_adj):
    min_vertex = None
    min_distance = sys.maxsize
    
    for v in q:
        if distance_for_adj[v] < min_distance:
            min_distance = distance_for_adj[v]
            min_vertex = q[v]
    if min_vertex.id in(q):    
        del q[min_vertex.id]

    return min_vertex


def relax(u, v, distance_for_adj, pi):
    if distance_for_adj[v.id] > distance_for_adj[u.id] + u.get_adj_weight(v):
        distance_for_adj[v.id] = distance_for_adj[u.id] + u.get_adj_weight(v)
        pi[v.id] = u

def print_dijkstra_output(graph, s, pi, distance_for_adj):
    print('dijkstra results - find shortest paths from root {}'.format(s.id))

    for v in graph.keys():
        if v != s.id:
            print('vertex {} has distance of {} from the root {} and pi: {}.'
                .format(v, distance_for_adj[v], s.id, pi[v].id))
        else:
            print('vertex {} is root vertex and has distance of {} from himself and {} pi.'
                .format(v, distance_for_adj[v], pi[v]))
    print('The End :)')

if __name__ == "__main__":
    input_graph = Graph()

    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')
    h = Vertex('H')
    s = Vertex('S')

    input_graph.add_vertex(a)
    input_graph.add_vertex(b)
    input_graph.add_vertex(c)
    input_graph.add_vertex(d)
    input_graph.add_vertex(e)
    input_graph.add_vertex(f)
    input_graph.add_vertex(h)
    input_graph.add_vertex(s)

    input_graph.add_edge(s, a, 33)
    input_graph.add_edge(s, c, 10)
    input_graph.add_edge(s, b, 8)
    input_graph.add_edge(a, e, 11)
    input_graph.add_edge(c, f, 9)
    input_graph.add_edge(c, h, 13)
    input_graph.add_edge(c, d, 6)
    input_graph.add_edge(b, d, 12)
    input_graph.add_edge(f, a, 3)
    input_graph.add_edge(f, e, 25)
    input_graph.add_edge(h, f, 6)
    input_graph.add_edge(d, h, 5)

    dijkstra(input_graph, s)