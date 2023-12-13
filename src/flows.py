from itertools import *
from igraph import *
import VectorR

def graph_flows_brute(G: Graph, vector, comparator_equal, comparator_lesser_than, comparator_bigger_than, addition,
                      neutral_element):
    produc = product(vector,repeat =G.ecount())
    temp = None
    for c in produc:
        G.es['weight'] = list(c)
        if check_flow(G, addition, comparator_equal):
            if temp is None:
                temp = find_biggest(G, vector, comparator_equal, comparator_bigger_than)
                continue
            temp2 = find_biggest(G, vector, comparator_equal, comparator_bigger_than)
            if comparator_lesser_than(temp2, temp):
                temp = temp2
    return temp

def find_biggest(G: Graph, vector, comparator_equal, comparator_bigger_than):
    weights = G.es["weight"]
    bigest = None
    for i in range(len(weights)):
        if bigest is None:
            bigest = weights[i]
            continue
        if comparator_bigger_than(weights[i], bigest) or comparator_equal(weights[i], bigest):
            bigest = weights[i]
    return bigest


def check_flow(G: Graph, addition, comparator_equal):
    for v in G.vs:
        in_edges_sum = None
        for edgein in v.in_edges():
            if in_edges_sum is None:
                in_edges_sum = edgein["weight"]
                continue
            in_edges_sum = addition(in_edges_sum, edgein["weight"])
        out_edges_sum = None
        for edgeout in v.out_edges():
            if out_edges_sum is None:
                out_edges_sum = edgeout["weight"]
                continue
            out_edges_sum = addition(out_edges_sum, edgeout["weight"])
        if comparator_equal(in_edges_sum, out_edges_sum):
            continue
        return False
    return True
