from numba import jit
from itertools import product
@jit(nopython=True,cache=True,nogil=True)
def if_greater_than_one(a,b,c,d):
    left_expression = (a * a) + (2 * b * b) + (c * c) + (2 * d * d) - 1
    right_expression = -((a * b) + (c * d))
    if left_expression < 0 and right_expression >= 0:
        return False
    if left_expression >= 0 and right_expression < 0:
        return True
    if left_expression < 0 and right_expression < 0:
        return left_expression ** 2 <= 8 * (right_expression ** 2)
    return left_expression ** 2 >= 8 * (right_expression ** 2)

@jit(nopython=True,cache=True,nogil=True)
def if_lesser_than_x(a,b,c,d,x):
    left_expression = (a * a) + (2 * b * b) + (c * c) + (2 * d * d) - (x*x)
    right_expression = -((a * b) + (c * d))
    if left_expression < 0 and right_expression >= 0:
        return True
    if left_expression >= 0 and right_expression < 0:
        return False
    if left_expression < 0 and right_expression < 0:
        return left_expression ** 2 >= 8 * (right_expression ** 2)
    return left_expression ** 2 <= 8 * (right_expression ** 2)


@jit(nopython=True,cache=True,nogil=True)
def comparator_equal(vector1, vector2):
    a, b, c, d = vector1
    e, f, g, h = vector2
    left_expression = (a * a) + (2 * b * b) + (c * c) + (2 * d * d) - ((e * e) + (2 * f * f) + (g * g) + (2 * h * h))
    right_expresion = (e * f) + (g * h) - (a * b) - (c * d)
    return left_expression**2 == 8*(right_expresion**2)

@jit(nopython=True, cache=True, nogil=True)
def adition(vector1, vector2):
    a, b, c, d = vector1
    e, f, g, h = vector2
    return [a + e, b + f, c + g, d + h]

@jit(nopython=True, cache=True, nogil=True)

def difference(vector1, vector2):
    a, b, c, d = vector1
    e, f, g, h = vector2
    return [a - e, b - f, c - g, d - h]
@jit(nopython=True, cache=True, nogil=True)
def neutral_element():
    return [0, 0, 0, 0]

@jit(nopython=True, cache=True, nogil=True)
def comparator_lesser(vector1,vector2):
    a,b,c,d = vector1
    e,f,g,h = vector2
    left_expression = (a * a) + (2 * b * b) + (c * c) + (2 * d * d)-((e * e) + (2 * f * f) + (g * g) + (2 * h * h))
    right_expresion = (e*f)+(g*h)-(a*b)-(c*d)
    if left_expression < 0 and right_expresion >= 0:
        return True
    if left_expression >= 0 and right_expresion < 0:
        return False
    if left_expression < 0 and right_expresion < 0:
        return left_expression ** 2 > 8 * (right_expresion ** 2)
    return left_expression ** 2 < 8 * (right_expresion ** 2)

@jit(nopython=True, cache=True, nogil=True)
def comparator_bigger(vector1, vector2):
    a, b, c, d = vector1
    e, f, g, h = vector2
    left_expression = (a * a) + (2 * b * b) + (c * c) + (2 * d * d)-((e * e) + (2 * f * f) + (g * g) + (2 * h * h))
    right_expresion = (e*f)+(g*h)-(a*b)-(c*d)
    if left_expression < 0 and right_expresion >= 0:
        return False
    if left_expression >= 0 and right_expresion < 0:
        return True
    if left_expression < 0 and right_expresion < 0:
        return left_expression ** 2 < 8 * (right_expresion ** 2)
    return left_expression ** 2 > 8 * (right_expresion ** 2)

def generate_vector_R(fro, to, x):
    for i in product(range(fro, to + 1), repeat=4):
        if if_greater_than_one(i[0], i[1], i[2], i[3]) and if_lesser_than_x(i[0], i[1], i[2], i[3], x):
            yield i
