import copy
import random


def mat_zeros(m, n):
    return [[0] * n for i in range(m)]


def mat_ones(m, n):
    return [[1] * n for i in range(m)]


def mat_rand(m, n):
    return [[random.random() for i in range(n)] for j in range(m)]


def mat_identity(size):
    res = mat_zeros(size, size)

    for i in range(size):
        res[i][i] = 1
    return res


def mat_transp(matr):
    m, n = mat_shape(matr)
    res = mat_zeros(m, n)
    for i in range(m):
        for j in range(n):
            res[i][j] = matr[j][i]
    return res


def mat_mul(m1, m2):
    m = len(m1)
    n1 = len(m1[0])
    n2 = len(m2)
    p = len(m2[0])

    if n1 != n2:
        raise ValueError("Matrix sizes mismatch for multiplication")

    # resulting matrix is m x p
    res = [[] * p] * m

    for i in range(m):
        for j in range(p):
            res[i][j] = sum(m1[i][k] * m2[k][i] for k in range(n1))

    return res


def mat_mul_scalar(matr, scalr):
    m, n = mat_shape(matr)
    for i in range(m):
        for j in range(n):
            matr[i][j] *= scalr


def mat_shape(matr):
    m = len(matr)
    n = len(matr[0])
    return m, n


def mat_print(matr, decimals = 3):
    m, n = mat_shape(matr)
    print("--- Matrix [%d x %d] ---" % (m, n))
    for i in range(m):
        for j in range(n):
            print(round(matr[i][j], decimals), end=" ")
        print()
    print()


def mat_det(matr):
    mc = copy.deepcopy(matr)
    m, n = mat_shape(mc)
    if m != n:
        raise ValueError("Matrix sizes mismatch for det calculation!")

    factors = 1
    for i in range(m - 1):
        j = i
        for inext in range(i + 1, m):
            if mc[inext][j] == 0:
                continue

            factor = mc[i][j] / mc[inext][j]
            factors *= factor
            for jiter in range(j, m):
                mc[inext][jiter] *= factor

            for jiter in range(j, m):
                mc[inext][jiter] -= mc[i][jiter]

    d = 1
    for i in range(m):
        d *= mc[i][i]

    d /= factors
    return d




# class vec:
#     def __init__(self, size, is_col = True):
#         self.data = [0] * size
#         self.is_col = is_col
#
#
# class mat:
#     # Creates a matrix of size X size filled in with zeros.
#     def __init__(self, size):
#         self.data = [[]] * size
#         self.m = size
#         self.n = size
#
#         for i in range(size):
#             self.data[i] = [0] * size
#
#
    # def print(self):
    #     print("Size =", self.m, "X", self.n)
    #
    #     for i in range(self.m):
    #         for j in range(self.n):
    #             print(self.data[i][j], end = " ")
    #
    #         print()
#
# def mul(m1, m2):
#     m1_row_count = len(m1)
#     m2_row_count = len(m2)
#     assert m1_row_count == m2_row_count
#     # M1 = M x N; M2 = N X P; result = M X P


def slice(a, skipj):
    res = copy.deepcopy(a)
    for i in range(1, len(a)):
        res[i].pop(skipj)
    res.pop(0)

    return res


def det(a):
    m, n = len(a), len(a[0])
    if m != n:
        raise ValueError("Incompatible matrix dimensions!")

    if m == 2 and n == 2:
        return a[0][0] * a[1][1] - a[1][0] * a[0][1]

    # we always develop on the first row in the matrix
    first_row = a[0]
    sum = 0
    for j in range(n):
        elem = first_row[j]
        jminor = slice(a, j)
        sum += elem * det(jminor)
    return sum


# Matrix is at least 3x3 in size. First call is with empty skipcols
# def det_r(a, i, skipcols):
#     sc = copy.deepcopy(skipcols)
#     m, n = len(a), len(a[0])
#     s = 0
#     for j in range(n):
#         if j in skipcols:
#             continue
#         sc.append(j)
#         s += a[i][j] * det_r(a, i + 1, sc)
#
#     return s
#
#
# def det2(a):
#     m, n = len(a), len(a[0])
#
#     if m != n:
#         raise ValueError("Incompatible matrix dimensions!")
#
#     if m == 1:
#         return a[0][0]
#
#     if m == 2:
#         return a[0][0] * a[1][1] - a[1][0] * a[0][1]
#
#     return det_r(a, 0, [])

