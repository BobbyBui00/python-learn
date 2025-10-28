print(range(100)) ## range(0, 100)

for number in range(100):
    print(number)

## use _ if you don't need to use the iterated value
for _ in range(100):
    print('Hello')

for _ in range(0, 10, 2):
    print(_) ## _ can be used as a variable
    ## 0, 2, 4, 6, 8

for _ in range(0, 10, -1):
    print(_) ## empty result

for _ in range(10, 0, -1):
    print(_) ## in reverse order from 10 to 0

for _ in range(2):
    print(list(range(10)))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]