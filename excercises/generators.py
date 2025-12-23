## Create a Fibonaci function


## Generator    ##
def fib_generator(n):
    first_value = 0
    second_value = 1
    for _ in range(n):
        yield first_value
        next_value = first_value + second_value
        first_value = second_value
        second_value = next_value


for num in fib_generator(20):
    print(num)

print('***' * 10)


## List     ##
def fib_list(n):
    first_value = 0
    second_value = 1
    fibs = []
    for _ in range(n):
        fibs.append(first_value)

        next_value = first_value + second_value
        first_value = second_value
        second_value = next_value
    return fibs


print(fib_list(20))
