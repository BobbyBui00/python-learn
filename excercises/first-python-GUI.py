picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

## encounter 0 -> display Empty space
## encounter 1 -> display *

i = 0
while i < len(picture):
    line = picture[i]
    for item in line:
        if item == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print('')
    i += 1


## clean code: following a style Python community endorse
# 1/ Clean
# 2/ Readability
# 3/ Predictability
# 4/ DRY


#### IMPROVE CODE
FILL = '*'
EMPTY = ' '
for row in picture:
    for pixel in row:
        if pixel: ## truthy value -> false is value == 0
            print(FILL, end='')
        else:
            print(EMPTY, end='')
    print('')



### EXERCISE 2: Check duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# use data structure
new_list = list(set(some_list)) ## ['n', 'd', 'a', 'm', 'c', 'b']
for item in new_list:
    if some_list.count(item) == 1:
        continue
    else:
        print(item, end=' ')
print('')

# Do not use data structure
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)