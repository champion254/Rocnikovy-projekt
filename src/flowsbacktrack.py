from numba import njit


def graph_flow_backtrack(backtrack_matrix):
    backtrack_matrix.pop()
    return backtrack_matrix


def dive_into(matrix, backtrack_matrix, vector, addition, difference, neutral_element, depth):
    if (depth == 0):
        backtrack_matrix.append(list())
        for i in range(len(matrix)):
            temp = neutral_element()
            if (matrix[i][depth] == 1):
                temp = addition(temp, vector)
                backtrack_matrix[depth].append(temp)
                continue
            if (matrix[i][depth] == -1):
                temp = difference(temp, vector)
                backtrack_matrix[depth].append(temp)
                continue
            if (matrix[i][depth] == 0):
                backtrack_matrix[depth].append(temp)
        return backtrack_matrix
    backtrack_matrix.append(list())
    reading_depth = depth - 1
    for i in range(len(matrix)):
        temp = backtrack_matrix[reading_depth][i]
        if (matrix[i][depth] == 1):
            temp = addition(temp, vector)
            backtrack_matrix[depth].append(temp)
            continue
        if (matrix[i][depth] == -1):
            temp = difference(temp, vector)
            backtrack_matrix[depth].append(temp)
            continue
        if (matrix[i][depth] == 0):
            backtrack_matrix[depth].append(temp)
    return backtrack_matrix

def graph_flow_is_valid(backtrack_matrix, good_element, depth):
    for i in backtrack_matrix:
        if not good_element(i):
            return False
    return True


def calculate_best_flows(generator, matrix, comparator_equal, comparator_lesser_than, comparator_bigger_than, addition,
                         difference, neutral_element, good_element):
    backtrack_matrix = []
    depth = -1
    vectors = VectorofGenerators(generator, len(matrix[0]))
    best_vector = None
    original_vectors = list()
    for vector in vectors:
        if depth+1 == len(matrix[0]):
            best_vector = best_vector_find(backtrack_matrix[-1] + original_vectors, best_vector, good_element
                                          ,comparator_bigger_than, comparator_lesser_than)
        if depth >= vector[0]:
            while depth != vector[0]-1:
                graph_flow_backtrack(backtrack_matrix)
                original_vectors.pop()
                depth -= 1
        if depth < vector[0]:
            depth += 1
            original_vectors.append(vector[1])
            dive_into(matrix, backtrack_matrix, vector[1], addition, difference, neutral_element, depth)
            continue
    if depth + 1 == len(matrix[0]):
        best_vector = best_vector_find(backtrack_matrix[-1] + original_vectors, best_vector, good_element
                                  ,comparator_bigger_than, comparator_lesser_than)
    return best_vector

def best_vector_find(list,best_vector,good_element,comparator_bigger_than,comparator_lesser_than):
    if graph_flow_is_valid(list, good_element, 0):
        if best_vector is None:
            best_vector = find_biggest_element(list, comparator_bigger_than)
            return best_vector
        temp = find_biggest_element(list, comparator_bigger_than)
        if comparator_lesser_than(temp, best_vector):
            best_vector = temp
    return best_vector
def VectorofGenerators(generatorfunction, size):
    depth = 0
    #size += 1

    def recursion(generatorfunction, depthrec):
        if depthrec == size:
            return
        for i in generatorfunction():
            yield depthrec, i
            yield from recursion(generatorfunction, depthrec + 1)

    for i in generatorfunction():
        yield depth, i
        yield from recursion(generatorfunction, depth + 1)


def find_biggest_element(vectors, comparator_bigger_than):
    temp = None
    for i in vectors:
        if temp is None:
            temp = i
            continue
        if comparator_bigger_than(i, temp):
            temp = i
    return temp
