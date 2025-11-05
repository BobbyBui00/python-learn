# Scope - What variables do I have access to?

total = 100


def some_func():
    global total
    total = 10


print(f'Before: {total}')
some_func()
print(f'After: {total}')

# 1 - Start with local
# 2 - If local doesn't have that variable -> check parent local
# 3 - Global
# 4 - Built-in python functions
