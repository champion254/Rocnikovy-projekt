from flows import create_wheel_graph, create_matrix,graphs_flow
from flowsbacktrack import calculate_best_flows
from VectorR import *

limit = 5
minimum = 1
smallest_vector = [100, 0, 0, 0]
#test W3 for growing n
# print("W3")
for n in range(minimum, limit):
    G = create_wheel_graph(4)
    matrix = [[1,-1,0],[0,-1,-1],[1,0,-1]]
    print(matrix)
    a = [i for i in generate_vector_R_smaller_than_vector(-n, n, smallest_vector)]
    gentemp = [i for i in generate_vector_R_smaller_than_vector(-n, n, smallest_vector)]
    gen = lambda: iter(gentemp)
    print("n = ", n)
    smallest_vector = calculate_best_flows(gen, matrix, comparator_equal, comparator_lesser, comparator_bigger, adition,
                               difference, neutral_element, lambda x: if_greater_than_one(*x))
    small = graphs_flow(gen, matrix, comparator_equal, comparator_lesser, comparator_bigger, adition, difference, neutral_element, lambda x: if_greater_than_one(*x))
    print("normal",small[0])
    print("backtrack",smallest_vector[0])
    print("graph flow backtrack",smallest_vector[1])
    print("graph_normal",small[1])
    print("done")

#test W5 for growing n
# print("W5")
# for n in range(minimum, limit):
#     G = create_wheel_graph(5)
#     matrix = create_matrix(G)
#     print(matrix)
#     gen = lambda: generate_vector_R(-n, n, 1.5)
#     print("n = ", n)
#     print(calculate_best_flows(gen, matrix, comparator_equal, comparator_lesser, comparator_bigger, adition,
#                                difference, neutral_element, lambda x: if_greater_than_one(*x)))
#     print("done")
