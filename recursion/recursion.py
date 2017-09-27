def factorial(x):
    return x * factorial(x - 1)

#print(factorial(5654321314654606465465464654654323235464646465654665465446543131656465))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(4))

nums = {1, 2, 1, 3, 1, 4, 5, 6}

print(nums)