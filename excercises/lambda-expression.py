import math

my_list = [5, 4, 3]

# Square
print(list(map(lambda item: math.pow(item, 2), my_list)))

# List sorting - sort based on the second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda x: x[1]))
a.sort(key=lambda x: x[1])
print(a)
