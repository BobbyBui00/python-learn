# Create function called highest even
# This function is going to take a list of data type
# and this function pass
# print(highest_even([10, 2, 3, 4, 8, 11]))

def highest_even(*args):
    evens = []
    for item in args[0]:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([2, 10, 2, 3, 4, 8, 11, 100]))
