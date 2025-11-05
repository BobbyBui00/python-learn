# *arg vs **kwargs
# *args: can accept any number positional arguments
# args is a tuple
# **kwargs: get any keywords and values
# kwargs receive as a dictionary

def super_func(*args, **kwargs):
    print(args)
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# Rule of thumb
# parameters -> *arg -> default parameter -> **kwargs
def some_func(name, *arg, i='hi', **kwargs):
    print(name)
    print(arg)
    print(i)
    print(kwargs)


some_func('Andy', 1, 2, 3, 4, 5, i='hello', num1=5, num2=10)
some_func('Andy', 1, 2, 3, 4, 5, num1=5, num2=10)
