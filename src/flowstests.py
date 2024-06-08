import unittest

from igraph import *

from flows import create_matrix
from flowsbacktrack import *


class MyTestCase(unittest.TestCase):
    def test_flows_backtrack(self):
        list = [[1, 2, 3], [4, 5, 6]]
        graph_flow_backtrack(list)
        self.assertEqual(list, [[1, 2, 3]])
        graph_flow_backtrack(list)
        self.assertEqual(list, [])

    def test_dive_into1(self):
        matrix = [[1, 0, 1], [-1, 1, 0]]
        backtrack_matrix = []
        number1 = 1
        number2 = 2
        __addition = lambda x, y: x + y
        __difference = lambda x, y: x - y
        __neutral_element = lambda: 0
        dive_into(matrix, backtrack_matrix, number1, __addition, __difference, __neutral_element, 0)
        self.assertEqual(backtrack_matrix, [[1, -1]])
        dive_into(matrix, backtrack_matrix, number2, __addition, __difference, __neutral_element, 1)
        self.assertEqual(backtrack_matrix, [[1, -1], [1, 1]])

    def test_dive_into2(self):
        matrix = [[1, 0, 1],
                  [-1, 1, -1],
                  [1, 0, 1]]
        backtrack_matrix = []
        number1 = 1
        number2 = 5
        number3 = 3
        __addition = lambda x, y: x + y
        __difference = lambda x, y: x - y
        __neutral_element = lambda: 0
        dive_into(matrix, backtrack_matrix, number1, __addition, __difference, __neutral_element, 0)
        self.assertEqual(backtrack_matrix, [[1, -1, 1]])
        dive_into(matrix, backtrack_matrix, number2, __addition, __difference, __neutral_element, 1)
        self.assertEqual(backtrack_matrix, [[1, -1, 1], [1, 4, 1]])
        dive_into(matrix, backtrack_matrix, number3, __addition, __difference, __neutral_element, 2)
        self.assertEqual(backtrack_matrix, [[1, -1, 1], [1, 4, 1], [4, 1, 4]])

    def test_dive_into3(self):
        matrix = [[1, 0, 1, 1],
                  [1, -1, 1, 0],
                  [1, 0, 0, -1],
                  [0, 0, -1, 1]]
        backtrack_matrix1 = []
        backtrack_matrix2 = []
        backtrack_matrix3 = []
        __addition = lambda x, y: x + y
        __difference = lambda x, y: x - y
        __neutral_element = lambda: 0
        dive_into(matrix, backtrack_matrix1, 1, __addition, __difference, __neutral_element, 0)
        self.assertEqual(backtrack_matrix1, [[1, 1, 1, 0]])
        dive_into(matrix, backtrack_matrix1, 2, __addition, __difference, __neutral_element, 1)
        self.assertEqual(backtrack_matrix1, [[1, 1, 1, 0], [1, -1, 1, 0]])
        dive_into(matrix, backtrack_matrix1, 10, __addition, __difference, __neutral_element, 2)
        self.assertEqual(backtrack_matrix1, [[1, 1, 1, 0], [1, -1, 1, 0], [11, 9, 1, -10]])
        dive_into(matrix, backtrack_matrix1, 11, __addition, __difference, __neutral_element, 3)
        self.assertEqual(backtrack_matrix1, [[1, 1, 1, 0], [1, -1, 1, 0], [11, 9, 1, -10], [22, 9, -10, 1]])

        dive_into(matrix, backtrack_matrix2, 2, __addition, __difference, __neutral_element, 0)
        self.assertEqual(backtrack_matrix2, [[2, 2, 2, 0]])
        dive_into(matrix, backtrack_matrix2, 5, __addition, __difference, __neutral_element, 1)
        self.assertEqual(backtrack_matrix2, [[2, 2, 2, 0], [2, -3, 2, 0]])
        dive_into(matrix, backtrack_matrix2, 15, __addition, __difference, __neutral_element, 2)
        self.assertEqual(backtrack_matrix2, [[2, 2, 2, 0], [2, -3, 2, 0], [17, 12, 2, -15]])
        dive_into(matrix, backtrack_matrix2, 16, __addition, __difference, __neutral_element, 3)
        self.assertEqual(backtrack_matrix2, [[2, 2, 2, 0], [2, -3, 2, 0], [17, 12, 2, -15], [33, 12, -14, 1]])

        dive_into(matrix, backtrack_matrix3, 3, __addition, __difference, __neutral_element, 0)
        self.assertEqual(backtrack_matrix3, [[3, 3, 3, 0]])
        dive_into(matrix, backtrack_matrix3, 7, __addition, __difference, __neutral_element, 1)
        self.assertEqual(backtrack_matrix3, [[3, 3, 3, 0], [3, -4, 3, 0]])
        dive_into(matrix, backtrack_matrix3, 9, __addition, __difference, __neutral_element, 2)
        self.assertEqual(backtrack_matrix3, [[3, 3, 3, 0], [3, -4, 3, 0], [12, 5, 3, -9]])
        dive_into(matrix, backtrack_matrix3, 10, __addition, __difference, __neutral_element, 3)
        self.assertEqual(backtrack_matrix3, [[3, 3, 3, 0], [3, -4, 3, 0], [12, 5, 3, -9], [22, 5, -7, 1]])

    def test_partial_graph_flow_is_valid(self):
        list_matrix_ones = [0, 1, 2, 3]
        good_element = lambda x: x > 0
        depth = 0
        list_backtrack_last = [1, 2, 3, 4]
        self.assertTrue(partial_graph_flow_is_valid(list_matrix_ones, good_element, depth, list_backtrack_last))
        list_backtrack_last = [0, 2, 3, 4]
        self.assertFalse(partial_graph_flow_is_valid(list_matrix_ones, good_element, depth, list_backtrack_last))
        depth = 1
        list_backtrack_last = [1, 0, 3, 4]
        self.assertFalse(partial_graph_flow_is_valid(list_matrix_ones, good_element, depth, list_backtrack_last))
        list_backtrack_last = [1, 2, 0, 4]
        self.assertTrue(partial_graph_flow_is_valid(list_matrix_ones, good_element, depth, list_backtrack_last))
        depth = 2
        list_backtrack_last = [1, 2, 3, 0]
        self.assertTrue(partial_graph_flow_is_valid(list_matrix_ones, good_element, depth, list_backtrack_last))
        list_backtrack_last = [1, 2, 3, 5]
        self.assertTrue(partial_graph_flow_is_valid(list_matrix_ones, good_element, depth, list_backtrack_last))

    def test_graph_flow_depth_check_generate_list(self):
        matrix = [[1, 0, 1],
                  [1, -1, 1],
                  [1, 0, 0]]
        self.assertEqual(graph_flow_depth_check_generate_list(matrix), [2, 2, 0])
        matrix = [[1, 0, 1, 1],
                  [1, -1, 1, 0],
                  [1, 0, 0, -1],
                  [0, 0, 0, 0]]
        self.assertEqual(graph_flow_depth_check_generate_list(matrix), [3, 2, 3, []])

    def test_Vector_of_generators(self):
        generator_function = lambda: range(3)
        list = []
        generator = VectorofGenerators(generator_function, 3, list)
        for i in range(3):
            self.assertEqual(next(generator), (0, i))
            for j in range(3):
                self.assertEqual(next(generator), (1, j))
                for k in range(3):
                    self.assertEqual(next(generator), (2, k))
        self.assertRaises(StopIteration, next, generator)

        generator = VectorofGenerators(generator_function, 3, list)
        for i in range(3):
            self.assertEqual(next(generator), (0, i))
            for j in range(3):
                self.assertEqual(next(generator), (1, j))
                for k in range(3):
                    if (k == 0):
                        list.append(1)
                        break
                    self.assertEqual(next(generator), (2, k))
        self.assertRaises(StopIteration, next, generator)

    def test_best_vector_find(self):
        good_element = lambda x: x > 5
        comparator_bigger_than = lambda x, y: x > y
        comparator_lesser_than = lambda x, y: x < y
        self.assertEqual(best_vector_find([5, 10, 15], None, good_element, comparator_bigger_than,
                                          comparator_lesser_than), None)
        self.assertEqual(best_vector_find([10, 15], None, good_element, comparator_bigger_than,
                                          comparator_lesser_than), 15)
        self.assertEqual(best_vector_find([6, 7, 8], 10, good_element, comparator_bigger_than,
                                          comparator_lesser_than), 8)

    def test_graph_flow_is_valid(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        list3 = [0, 8, 9]
        good_element = lambda x: x > 0
        self.assertTrue(graph_flow_is_valid(list1, good_element, 0))
        self.assertTrue(graph_flow_is_valid(list2, good_element, 1))
        self.assertFalse(graph_flow_is_valid(list3, good_element, 2))

    def test_calculate_best_flows(self):
        matrix = [[1, 1, 0],
                  [1, 1, 0]]
        list = []
        comparator_equal = lambda x, y: x == y
        comparator_lesser_than = lambda x, y: x < y
        comparator_bigger_than = lambda x, y: x > y
        addition = lambda x, y: x + y
        difference = lambda x, y: x - y
        neutral_element = lambda: 0
        good_element = lambda x: x > 0
        generator = lambda: range(3)
        self.assertEqual(calculate_best_flows(generator, matrix, comparator_equal, comparator_lesser_than,
                                              comparator_bigger_than, addition, difference, neutral_element,
                                              good_element), 2)
        good_element = lambda x: x > 3
        self.assertEqual(calculate_best_flows(generator, matrix, comparator_equal, comparator_lesser_than,
                                              comparator_bigger_than, addition, difference, neutral_element,
                                              good_element), None)
        generator = lambda: range(5)
        self.assertEqual(calculate_best_flows(generator, matrix, comparator_equal, comparator_lesser_than,
                                              comparator_bigger_than, addition, difference, neutral_element,
                                              good_element), 8)
        matrix = [[1, 1, -1],
                  [1, 1, -1]]
        self.assertEqual(calculate_best_flows(generator, matrix, comparator_equal, comparator_lesser_than,
                                              comparator_bigger_than, addition, difference, neutral_element,
                                              good_element), 4)

    def test_calculate_best_flows2(self):
        G = Graph(n=3, edges=[[0, 1], [1, 2], [2, 0]], directed=True)
        matrix = create_matrix(G)
        comparator_equal = lambda x, y: x == y
        comparator_lesser_than = lambda x, y: x < y
        comparator_bigger_than = lambda x, y: x > y
        addition = lambda x, y: x + y
        difference = lambda x, y: x - y
        neutral_element = lambda: 0
        good_element = lambda x: x > 3
        generator = lambda: range(5)
        self.assertEqual(calculate_best_flows(generator, matrix, comparator_equal, comparator_lesser_than,
                                              comparator_bigger_than, addition, difference, neutral_element,
                                              good_element), 4)

    def test_calculate_best_flows3(self):
        matrix = [[1, 0, 1],
                  [-1, 1, 0],
                  [1, 0, 1],
                  [-1, 0, 0]]
        comparator_equal = lambda x, y: x == y
        comparator_lesser_than = lambda x, y: x < y
        comparator_bigger_than = lambda x, y: x > y
        addition = lambda x, y: x + y
        difference = lambda x, y: x - y
        neutral_element = lambda: 0
        good_element = lambda x: x > 4
        generator = lambda: range(8)
        self.assertEqual(calculate_best_flows(generator, matrix, comparator_equal, comparator_lesser_than,
                                              comparator_bigger_than, addition, difference, neutral_element,
                                              good_element), None)


if __name__ == '__main__':
    unittest.main()
