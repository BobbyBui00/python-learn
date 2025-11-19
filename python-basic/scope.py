# Scope - What variables do I have access to?

total = 100


def some_func():
    global total
    total += 10


print(f'Before: {total}')
some_func()
print(f'After: {total}')

# 1 - Start with local
# 2 - If local doesn't have that variable -> check parent local
# 3 - Global
# 4 - Built-in python functions


### DEPENDENCY INJECTION ###
total_di = 0


def count_di(total_di):
    total_di += 1
    return total_di


print(f"Dependency Injection: {count_di(count_di(count_di(total_di)))}")


### NON LOCAL KEYWORD ###

def outer():
    x = "local"

    def inner():
        # don't use the x local variable, jump up to parent variable to get the x variable
        # if don't have nonlocal variable, it will create a new x variable independent of x variable in parent function
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()
