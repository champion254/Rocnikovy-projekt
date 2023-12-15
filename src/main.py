from igraph import *
import numpy as np
import VectorR
from flows import graph_flows_brute
from itertools import *

def main():
    # a = VectorR.generate_vector_R(-2, 2, 5)
    # a = list(a)
    # print(a)
    # print(len(a))

    G = Graph(n=5, edges=[[1,0], [1, 2],[3,2],[1,4],[0,3],[2,4],[4,3]],directed = True)
    print(create_matrix(G))
    print(graphs_flow(VectorR.generate_vector_R(-1,1,5),create_matrix(G),VectorR.comparator_equal, VectorR.comparator_lesser,
                VectorR.comparator_bigger, VectorR.adition, VectorR.difference, VectorR.neutral_element, is_good))
    #G = Graph(n=2, edges=[[0, 1], [1, 0]], directed=True)
    # result = graph_flows_brute(G, a, VectorR.comparator_equal, VectorR.comparator_lesser,
    #                                  VectorR.comparator_bigger, VectorR.adition, VectorR.neutral_element)
    # print(result)
    # print(create_matrix(G))

if __name__ == '__main__':
    main()
