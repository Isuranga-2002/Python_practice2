def filter_even(x):
  return x % 2 == 0

even_numbers = filter(filter_even, [1, 2, 3, 4, 5])

print(list(even_numbers)) 