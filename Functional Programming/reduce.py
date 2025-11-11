from functools import reduce

def multiply(x, y):
  return x * y
 
product = reduce(multiply, [1, 2, 3, 4, 5])

print(product) 