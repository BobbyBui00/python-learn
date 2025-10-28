## ENUMERATE - take an iterable object and gives you an index counter and the item of that index

for i, char in enumerate('Helllooo'):
    print(i, char)

for i, char in enumerate((1, 2, 3)):
    print(i, char)

for i, char in enumerate([1, 2, 3]):
    print(i, char)

## create a script to enumerate a list of numbers 1 through 10, and I want to be told what the index of the number 50 is
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of {char} is {i}")