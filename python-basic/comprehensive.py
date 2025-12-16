# List Comprehensive, Set Comprehensive, Dictionary Comprehensive

my_list = []

## instead of old school creation of list
for char in 'hello':
    my_list.append(char)

print(my_list)

### LIST COMPREHENSION  ###
## comprehensive let us create a list in a quicker way instead of looping
my_list = [param for param in 'hello']
my_list_2 = [num * 2 for num in range(0, 100)]
my_list_3 = [num ** 2 for num in range(0, 100)]
my_list_4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_list_2)
print(my_list_3)
print(my_list_4)

### SET COMPREHENSION   ###
my_set = {param for param in 'hello'}
my_set_2 = {num * 2 for num in range(0, 100)}
my_set_3 = {num ** 2 for num in range(0, 100)}
my_set_4 = {num ** 2 for num in range(0, 100) if num % 2 == 0}

print(my_set)
print(my_set_2)
print(my_set_3)
print(my_set_4)

### DICTIONARY COMPREHENSION    ###
simpleDictionary = {
    'a': 1,
    'b': 2
}
my_dict = {k: v ** 2 for k, v in simpleDictionary.items()}
my_dict_2 = {k: v ** 2 for k, v in simpleDictionary.items() if v % 2 == 0}
my_dict_3 = {num: num * 2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict_2)
print(my_dict_3)
