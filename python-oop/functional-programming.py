### Pure function - more of a guideline and an absolute
# has two rules:
# 1/ Given the same input, it will return the same output
# 2/ the pure function should not produce any side effect

def multiple_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list  # pure function - doesnt affect outside world and doesnt have side effect
    # return print(new_list) # not pure function - because it has side effect -> print the result, interact with outside world


print(multiple_by2([1, 2, 3]))


### map, filter, zip, and reduce

# map - pure function, return a new list, doesn't affect the outside world (or the original array that is passed in)
def multiple_by_2_map(item):
    return item * 2


print(list(map(multiple_by_2_map, [1, 2, 3])))  ## function here doesn't have the brackers ()
print(list(map(lambda item: item * 2, [1, 2, 3])))  ## function here doesn't have the brackers ()

# filter - pure function, return a new list, doesn't affect the outside world (or the original array that is passed in)
my_list = [1, 2, 3]

def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))

# zip
my_list_zip = [10, 20, 30]
your_list_zip = (1, 2, 3)
their_list = [11, 22]

print(list(zip(my_list_zip, your_list_zip, their_list)))

# reduce
from functools import reduce
my_list_reduce = [1, 2, 3]


# the value it returns will be used as an accumulator for the next call, the initial accumulator is set as the last
# parameter in the reduce() function
# reduce take two parameters: first param is an accumulator, second param is the item in the provided list
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list_reduce, 0))
