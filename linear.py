from numpy import matrix
from numpy import shape

vector_x = [[2, 5], [3, -8], [1, -20], [21, -9], [2, 9], [12, 6]]
vector_y = [[10, 3], [1, -5], [-2, -5], [8, -1], [-5, -8], [-8, 1]]

matrix_x = matrix(vector_x)
matrix_y = matrix(vector_y)

# print(matrix_x)
# print(matrix_y)
#
#
# def copy_vector(x, y):
#     assert type(x) == matrix and len(x.shape) == 2
#     m, n = shape(x)
#     for i in range(m):
#         for j in range(n):
#             y[i, j] = x[i, j]
#
#
# copy_vector(matrix_x, matrix_y)
# print(matrix_y)


def is_equal(x, y):
    try:
        # The matrix must be a 2D array
        assert type(x) is matrix and len(x.shape) is 2
        print("PASSED: x is a 2D matrix")
        assert type(y) is matrix and len(y.shape) is 2
        print("PASSED: y is a 2D matrix")

        m_x, n_x = x.shape
        m_y, n_y = y.shape
        if m_x == m_y and n_x == n_y:
            print("PASSED: x and y matrix length is equal")
            return True
        else:
            return False
    except AssertionError:
        print("Variable does not match in the required arguments")


def copy(x, y):
    if is_equal(x, y):
        m_x, n_x = x.shape
        for i in range(m_x):
            for j in range(n_x):
                y[i, j] = x[i, j]
        print("PASSED: completed the copy of x to y")


print(matrix_y == matrix_x)
copy(matrix_x, matrix_y)
print(matrix_y == matrix_x)