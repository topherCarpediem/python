#named function
def polynomial(x):
    return x**2 + 5*x + 4


print(polynomial(5))

# lambda
print((lambda x: x**2 + 5*x + 4)(5))


def call_twice(func, args):
    value = func(func(args))
    return value


exponent = call_twice(lambda args: args**2, 2)
print(exponent)

#mapping
nums = [11, 22, 33]
square_root = list(map(lambda x: x*x, nums))

print(square_root)

print(list(filter(lambda x: x % 2 == 0, nums)))


def coundown():
    i=5
    while i > 0:
        yield i
        i -= 1


print(list(coundown()))


def generate():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


for a in generate():
    print(a)
