from igraph import *
import numpy as np
import VectorR
from flows import graph_flows_brute


def main():
    a = VectorR.generate_vector_R(-2, 2, 5)
    print(a)
    print(len(a))
    # G = Graph(n=5, edges=[[1,0], [1, 2],[3,2],[1,4],[0,3],[2,4],[4,3]],directed = True)
    # print(create_matrix(G))
    # G = Graph(n=2, edges=[[0, 1], [1, 0]], directed=True)
    # result = graph_flows_brute(G, a, VectorR.comparator_equal, VectorR.comparator_lesser,
    #                                  VectorR.comparator_bigger, VectorR.adition, VectorR.neutral_element)
    # print(result)

def create_matrix(G:Graph):
    G_directed:Graph = G
    G_undirected:Graph = G.as_undirected()
    G_spanning_tree:Graph = G_undirected.spanning_tree()
    G_not_spanning_tree:Graph = (G_directed - G_spanning_tree.as_directed()).as_directed()
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
    return matrix.transpose()

def get_cut_of_vertices(G:Graph, vertice):
    se = {i for i in range(G.vcount())}
    [vertices, parents] = G.dfs(vid = vertice)
    final_set = se - set(vertices)
    ls = vertices
    return [ls,list(final_set)]

if __name__ == '__main__':
    main()
