# Tuple

# tuples are like lists, but unlike list, we cannot modify them -> immutable
# tuple are create define with (), while list is defined with []
# cannot sort, or reverse tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(5 in my_tuple)
#my_tuple[1] = 'z' ->  cannot assign to tuple, because it is immutable

# Benefit:
# if you dont need to change the list, that makes things easier because it tells other programmers this shouldnt be change
# make your code safer because people can modify it
# make code more predictable
# more performance, faster
# drawback:
# less flexible because we cannot sort a tuple, or run a reverse

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user.items())
# => return a list of tuples, return our key and value as a tuple
# Dictionary can have keys that are immutable, it is possible to have dictionary key as tuple
# Dictionary cannot have value as tuples, because it is mutable

user1 = {
    (1, 2): [1, 2, 3],
    'greet': 'hello'
}

print(user1[(1, 2)]) # -> [1, 2, 3]
# print(user1[0]) -> cannot do it because it is dictionary and it doesn't have index

new_tuple = my_tuple[1:2]
print(new_tuple) # -> (2,) -> tuple only have item tends to have comma at the end
print(my_tuple[1:3]) # -> (2, 3) -> no comma, because more than one item

x, y = my_tuple[1:3]
print(f"{x} - {y}")

x, y, *other, z = (1, 2, 3, 4, 5, 6, 7, 8)
print(f"{x} - {y} - {other} - {z}") # -> 1 - 2 - [3, 4, 5, 6, 7] - 8


### TUPLES METHOD ( COUNT() AND INDEX() )

my_tuple1 = (1, 2, 3, 4, 5, 6, 6)
print(my_tuple1.count(1)) # -> 1 -> 1 only appear once in the tuples
print(my_tuple1.count(6)) # -> 2 -> 6 appears twice in the tuples
print(my_tuple1.index(6)) # -> 5 -> return the first index
print(len(my_tuple1)) # 7