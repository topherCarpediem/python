import numpy as np

x = [2, 31, 53, 81, 5, 4, 18, 12, 25, 36, 45, 4]
y = [5, 8, 10, 54, 78, 10, 9, 12, 1, 20, 45, 5]

print(len(x) == len(y))

alpha_np = np.add(x, y) #Use numpy for fast computation

print(alpha_np) #Print the result

#Hard coded to get the alpha
alpha = []
if len(x) == len(y):
    for index in range(len(x)):
        alpha.append(x[index] + y[index])

#Print the alpha result
print(alpha)


