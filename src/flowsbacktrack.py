def graph_flow_backtrack(backtrack_matrix):
    backtrack_matrix.pop()
    return backtrack_matrix


def dive_into(matrix, backtrack_matrix, vector, addition, difference, neutral_element, depth):
    if depth == 0:
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


def graph_flow_depth_check_generate_list(backtrack_matrix):
    last_ones = [[]] * len(backtrack_matrix)
    for i in range(len(backtrack_matrix)):
        temp = [j for j in range(len(backtrack_matrix[i])) if backtrack_matrix[i][j] == 1
                or backtrack_matrix[i][j] == -1]
        temp = temp[-1] if len(temp) > 0 else []
        last_ones[i] = temp
    return last_ones


def graph_flow_is_valid(backtrack_matrix, good_element, depth):
    for i in backtrack_matrix:
        if not good_element(i):
            return False
    return True


def partial_graph_flow_is_valid(list_matrix_ones, good_element, depth, list_backtrack_last):
    for i in range(len(list_backtrack_last)):
        if i is list and len(i) == 0: continue
        if not good_element(list_backtrack_last[i]) and list_matrix_ones[i] == depth:
            return False
    return True


def calculate_best_flows(generator, matrix, comparator_equal, comparator_lesser_than, comparator_bigger_than, addition,
                         difference, neutral_element, good_element):
    backtrack_matrix = []
    list_matrix_ones = graph_flow_depth_check_generate_list(matrix)
    list = []
    depth = -1
    vectors = VectorofGenerators(generator, len(matrix[0]), list)
    best_vector = None
    original_vectors = []
    validflow = None
    for vector in vectors:
        if depth + 1 == len(matrix[0]):
            temp = best_vector
            best_vector = best_vector_find(backtrack_matrix[-1] + original_vectors, best_vector, good_element
                                           , comparator_bigger_than, comparator_lesser_than)
            if temp != best_vector:
                validflow = backtrack_matrix[-1] + original_vectors
        if depth >= vector[0]:
            while depth != vector[0] - 1:
                graph_flow_backtrack(backtrack_matrix)
                original_vectors.pop()
                depth -= 1
        if depth < vector[0]:
            depth += 1
            original_vectors.append(vector[1])
            dive_into(matrix, backtrack_matrix, vector[1], addition, difference, neutral_element, depth)
        if not partial_graph_flow_is_valid(list_matrix_ones, good_element, depth, backtrack_matrix[-1]):
            list.append(depth)
    if depth + 1 == len(matrix[0]):
        temp = best_vector
        best_vector = best_vector_find(backtrack_matrix[-1] + original_vectors, best_vector, good_element
                                       , comparator_bigger_than, comparator_lesser_than)
        if temp != best_vector:
            validflow = backtrack_matrix[-1] + original_vectors
    return best_vector,validflow


def best_vector_find(list, best_vector, good_element, comparator_bigger_than, comparator_lesser_than):
    if graph_flow_is_valid(list, good_element, 0):
        if best_vector is None:
            best_vector = find_biggest_element(list, comparator_bigger_than)
            return best_vector
        temp = find_biggest_element(list, comparator_bigger_than)
        if comparator_lesser_than(temp, best_vector):
            best_vector = temp
    return best_vector


def VectorofGenerators(generatorfunction, size, list):
    depth = 0

    def recursion(generatorfunction, depthrec):
        if depthrec == size:
            return
        for i in generatorfunction():
            if len(list) > 0 and depthrec > list[0]:
                return
            if (len(list) > 0 and depthrec == list[0]):
                list.pop(0)
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
