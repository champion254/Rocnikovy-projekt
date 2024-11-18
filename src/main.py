from igraph import *

import VectorR
from flowsbacktrack import *
from flows import create_matrix,graphs_flow

def main1():
    a = VectorR.generate_vector_R(-1, 1, 5)
    a = list(a)
    print(a)
    print(len(a))


def main2():
    G = Graph(n=5, edges=[[1, 0], [1, 2], [3, 2], [1, 4], [0, 3], [2, 4], [4, 3]], directed=True)
    print(create_matrix(G))
    matrix = create_matrix(G)
    result = graphs_flow(VectorR.generate_vector_R(-1, 1, 5), matrix, VectorR.comparator_equal,
                         VectorR.comparator_lesser, VectorR.comparator_bigger,
                         VectorR.adition, VectorR.difference, VectorR.neutral_element, good_element)
    print(result)

def main3():
    G = Graph(n=5, edges=[[1, 0], [1, 2], [3, 2], [1, 4], [0, 3], [2, 4], [4, 3]], directed=True)
    print(create_matrix(G))
    matrix = create_matrix(G)
    generator = lambda : VectorR.generate_vector_R(-2, 2, 5)
    result = calculate_best_flows(generator, matrix, VectorR.comparator_equal,
                         VectorR.comparator_lesser, VectorR.comparator_bigger,
                         VectorR.adition, VectorR.difference, VectorR.neutral_element, good_element)
    print(result)

def good_element(vector):
    if VectorR.if_greater_than_one(*vector) and VectorR.if_lesser_than_x(*vector, 5):
        return True
    return False

def main4():
    G = Graph(n=4, edges=[[0, 1], [0, 3], [0, 2], [1, 3], [3, 2], [2, 1]], directed=True)
    print(create_matrix(G))
if __name__ == '__main__':
    main4()
