# Written by:
# Sapir Holzman 318265097
# Shahaf Shavit 314967324


import sys
import copy

from Tar4.Graph import Graph, Vertex


def dijkstra(graph, s):
    distance_for_adj, pi = initialize_single_source(graph, s)
    S = []
    q = copy.deepcopy(graph.vertices)

    while len(q) > 0:
        u = extract_min(q, distance_for_adj)
        S.append(u)

        for v in u.adjacent:
            relax(u, graph.get_vertex(v['id']), distance_for_adj, pi)

    print_dijkstra_output(graph, s, pi, distance_for_adj)


def initialize_single_source(graph, s):
    distance_for_adj = {v_id: sys.maxsize for v_id in graph.vertices_ids}
    distance_for_adj[s.id] = 0

    pi = {v_id: None for v_id in graph.vertices_ids}

    return distance_for_adj, pi


def extract_min(q, distance_for_adj):
    min_vertex = None
    min_distance = sys.maxsize

    for v_id in q.keys():
        if distance_for_adj[v_id] < min_distance:
            min_distance = distance_for_adj[v_id]
            min_vertex = q[v_id]
    if min_vertex:
        del q[min_vertex.id]

    return min_vertex


def relax(u, v, distance_for_adj, pi):
    if distance_for_adj[v.id] > distance_for_adj[u.id] + u.get_adj_weight(v):
        distance_for_adj[v.id] = distance_for_adj[u.id] + u.get_adj_weight(v)
        pi[v.id] = u


def print_dijkstra_output(graph, s, pi, distance_for_adj):
    print('dijkstra results - find shortest paths from source vertex \'{}\': \n'.format(s.id))

    for v_id in graph.vertices_ids:
        if v_id != s.id:
            print('Vertex \'{}\' has distance of {} from the source and pi: \'{}\'.'
                  .format(v_id, distance_for_adj[v_id], pi[v_id].id))
        else:
            print('vertex \'{}\' is the source vertex and has distance of {} from itself and \'{}\' pi.'
                  .format(v_id, distance_for_adj[v_id], pi[v_id]))


if __name__ == '__main__':
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
