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

def create_matrix(G:Graph):
    G_directed:Graph = G
    G_undirected:Graph = G.as_undirected()
    G_spanning_tree:Graph = G_undirected.spanning_tree()
    G_not_spanning_tree:Graph = (G_directed - G_spanning_tree.as_directed())
    G_spanning_tree_edges = G_spanning_tree.get_edgelist()
    G_not_spanning_tree.es["label"] = [i for i in range(G_not_spanning_tree.ecount())]
    G_not_spanning_tree_edges = G_not_spanning_tree.get_edgelist()
    matrix = np.zeros((G_spanning_tree.ecount(),G_not_spanning_tree.ecount()))
    lst = []
    for i in G_spanning_tree_edges:
        G_spanning_tree.delete_edges(i)
        lst.append(get_cut_of_vertices(G_spanning_tree, i[0]))
        G_spanning_tree.add_edges([i])

    dc = {edge:i for i,edge in enumerate(G_not_spanning_tree_edges)}
    for index,i in enumerate(lst):
        set1 = set(i[0])
        set2 = set(i[1])
        for j in G_not_spanning_tree_edges:
            if j[0] in set1 and j[1] in set2:
                if j[0] < j[1]:
                    matrix[index][dc[j]] = 1
                if j[0] > j[1]:
                    matrix[index][dc[j]] = -1
                continue
            if j[0] in set2 and j[1] in set1:
                if j[0] < j[1]:
                    matrix[index][dc[j]] = 1
                if j[0] > j[1]:
                    matrix[index][dc[j]] = -1
    return matrix

def get_cut_of_vertices(G:Graph, vertice):
    se = {i for i in range(G.vcount())}
    [vertices, parents] = G.dfs(vid = vertice)
    final_set = se - set(vertices)
    ls = vertices
    return [ls,list(final_set)]

def graphs_flow(generator, matrix,comparator_equal, comparator_lesser_than, comparator_bigger_than, addition,
                       difference,neutral_element,good_element):
    produc = product(generator,repeat = matrix[0].size)
    temp_lowest = None
    for c in produc:
        temp_biggest = None
        for i in range(len(matrix)):
            temp = None
            for j in range(len(matrix[i])):
                if temp is None:
                    temp = c[j]
                    continue
                if matrix[i][j] == 1:
                    temp = addition(temp,c[j])
                if matrix[i][j] == -1:
                    temp = difference(temp,c[j])
            if not good_element(temp):
                continue
            if temp_biggest is None:
                temp_biggest = temp
                continue
            if comparator_bigger_than(temp,temp_biggest):
                temp_biggest = temp
        if temp_lowest is None:
            temp_lowest = temp_biggest
            continue
        if temp_biggest is not None and comparator_lesser_than(temp_biggest,temp_lowest):
            temp_lowest = temp_biggest
            print(temp_lowest)
    return temp_lowest