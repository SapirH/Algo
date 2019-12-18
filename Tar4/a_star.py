# Written by:
# Sapir Holzman 318265097
# Shahaf Shavit 314967324


import sys
import copy

from Graph import Graph, Vertex


def a_star(graph, s):
    S = []
    distance_for_adj, pi = initialize_single_source(graph, s)
    q = copy.deepcopy(graph.vertices)

    while len(q) > 0:
        u = extract_min(q, distance_for_adj)
        S.append(u)
        for v in u.adjacent:
            relax(u, q[v['id']], distance_for_adj, pi)

    print_a_star_output(graph, s, pi, distance_for_adj)


def initialize_single_source(graph, s):
    distance_for_adj = {v_id: sys.maxsize for v_id in graph.vertices_ids}
    distance_for_adj[s.id] = 0

    pi = {v_id: None for v_id in graph.vertices_ids}

    return distance_for_adj, pi


def extract_min(q, distance_for_adj):
    min_vertex = None
    min_distance = sys.maxsize

    for v_id in q.keys():
        if distance_for_adj[v_id] + q[v_id].heuristic_weight < min_distance:
            min_distance = distance_for_adj[v_id] + q[v_id].heuristic_weight
            min_vertex = q[v_id]
    if min_vertex:
        del q[min_vertex.id]

    return min_vertex


def relax(u, v, distance_for_adj, pi):
    if distance_for_adj[v.id] > distance_for_adj[u.id] + u.get_adj_weight(v) + v.heuristic_weight:
        distance_for_adj[v.id] = distance_for_adj[u.id] + u.get_adj_weight(v)
        pi[v.id] = u


def print_a_star_output(graph, s, pi, distance_for_adj):
    print('a star results - find shortest paths from root {}'.format(s.id))

    for v in graph.vertices_ids:
        if v != s.id:
            print('Vertex {} has distance of {} from the source vertex and pi: {}.'
                  .format(v, distance_for_adj[v], pi[v].id))
        else:
            print('Vertex {} is source vertex and has distance of {} from itself and {} pi.'
                  .format(v, distance_for_adj[v], pi[v]))


if __name__ == '__main__':
    input_graph = Graph()
    heuristic_weight_dict = {'A': 7, 'B': 7, 'C': 5, 'D': 3.5, 'E': 6, 'F': 3, 'H': 0, 'S': 9}

    a = Vertex('A', heuristic_weight_dict['A'])
    b = Vertex('B', heuristic_weight_dict['B'])
    c = Vertex('C', heuristic_weight_dict['C'])
    d = Vertex('D', heuristic_weight_dict['D'])
    e = Vertex('E', heuristic_weight_dict['E'])
    f = Vertex('F', heuristic_weight_dict['F'])
    h = Vertex('H', heuristic_weight_dict['H'])
    s = Vertex('S', heuristic_weight_dict['S'])

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

    a_star(input_graph, s)
