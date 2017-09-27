import array

x = [[2, 5], [3, -8], [1, -20], [21, -9], [2, 9], [12, 6]]
y = [[10, 3], [1, -5], [-2, -5], [8, -1], [-5, -8], [-8, 1]]

vector_len = []
x_scale = [[] for i in range(len(x))]
subtract = [[] for j in range(len(x))]
alpha = [[] for index in range(len(x))]
dot_prod = 0


# ax+y where a is alpha times vector x plus vector y
def axpy(x_vector, y_vector, factor):
    for index in range(len(x)):
        for item in range(len(x[index])):
            scale = x_vector[index][item] * factor
            alpha[index].append(scale + y_vector[index][item])


def subtract_vector(x, y):
    for i in range(len(x)):
        for j in range(len(x[i])):
            subtract[i].append(x[i][j] - y[i][j])


# a*x
def scale_vector(vector, factor):
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            x_scale[i].append(vector[i][j] * factor)


def dot_product(x_vector, y_vector):
    for index in range(len(x)):
        for item in range(len(x[index])):
            scale = x_vector[index][item] * y_vector[index][item]
            global dot_prod
            dot_prod += scale


def vector_length(vector):
    point_x = 0
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            if j != 2:
                point_x = vector[i][j]
            else:
                point_y = vector[i][j]
                print((lambda x1, y1: float((x1 ** 2 + y1 ** 2)) ** .5)(point_x, point_y))


axpy(x, y, 2)
scale_vector(x, 1/2)
subtract_vector(x, y)
dot_product(x, y)
vector_length(y)

print(alpha)
print(x_scale)
print(subtract)
print(dot_prod)
print(vector_len)
