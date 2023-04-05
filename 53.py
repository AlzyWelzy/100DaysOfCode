from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l)

newl = list(map(lambda x: x**2, l))

print(newl)

newl = list(filter(lambda x: x % 2 == 0, l))

print(newl)

newl = reduce(lambda x, y: x + y, l)

print(newl)
