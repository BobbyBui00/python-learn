# Python's Dictionary data type equivalent to other language's HashMap. It is a data type but also a data structure
## It is un-ordered key-pair. Each elements are not standing near to each other.
dictionary = {
    'a': 1,
    'b': 2,
    'x': 4
}

print(dictionary['b'])
#print(dictionary['c']) ## KeyError
print(dictionary)

dictionary1 = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'x': True
}
print(dictionary1['a']) # [1, 2, 3]
print(dictionary1['a'][1]) # 2

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'Hello',
        'x': True
    },
]
print(my_list[0]['a'][2])
print(my_list[0]['a'][1])


### WHEN TO USE LIST VS DICTIONARY
# 1/ LIST:
# ordered
# store indexes and its value

# 2/ DICTIONARY
# unordered
# store more information than list with key and value pair. It values can store any data type


### DICTIONARY KEYS
dictionary = {
   123: [1, 2, 3],
   True: 'hello',
   # [100]: True,
   '[100]': {'a': True}
}
print(dictionary[123])
print(dictionary[True])
#print(dictionary[[100]]) # TypeError - because dictionary key must be immutable while list is mutable
print(dictionary['[100]'])

duplication_key_dict = {
    '123': [1, 2, 3],
    '123': 'hello'
}
print(duplication_key_dict['123']) # hello - cause it will be override -> dictionary key must be unique

# DICTIONARY METHODS

user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}
print(user.get('age')) # None
print(user.get('age', 24)) # grab the key in the dictionary, if there is no such key in dictionary, use the provide as value, else use the value in the dictionary

user2 = dict(name='JohnJohn')
print(user2)

print('basket' in user) # True
print('size' in user) # False
print('hello' in user) # False
print('hello' in user.values()) # True
print('hello' in user.keys()) # False
print(user.items())

# clear()
user2.clear()
print(user2) # equivalent to print(user2.clear())

# copy()

user2 = user.copy()
print(user)
print(user2)

# pop()
print(user2.pop('greet'))

# popitem()
print(user.popitem()) # remove the last key: value pair insert to the dict
print(user)

# update()
dict = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}
print(dict)
print(dict.update({'age': 55}))
print(dict)