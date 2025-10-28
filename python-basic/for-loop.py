for item in 'Zero to Mastery':
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in {1, 2, 3, 4, 5}:
    print(item)

for item in (1, 2, 3, 4, 5):
    print(item)

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)

## iterable - can be list, dictionary, tuple, set, string
# iterate -> one by one check each item in the collection

user = {
    "name": 'Golem',
    "age": 5006,
    "can_swim": False
}

for item in user.items():
    print(item) ## print the key pair value in the tuples format

for item in user.values():
    print(item) ## print the list of values

for item in user.keys():
    print(item) ## print the list of keys

for item in user.items():

    print(key, value)

for key, value in user.items():
    print(key, value)

for k, v in user.items():
    print(k, v)

for item in user:
    print(item) ## print the key of dictionary
    print(user.get(item)) ## print the value of dictionary using item as key

