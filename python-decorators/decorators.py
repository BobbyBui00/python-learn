## @decorator - supercharge our functions and add extra functionality to it

## Higher Order Functions - HOC
# 1/ function that accept another function
# 2/ function that return another function

from time import time

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')

    return wrap_func


@my_decorator
def hello():
    print('Hello')


@my_decorator
def hello_with_greeting(greeting):
    print(greeting)


@my_decorator
def bye(last_word, emoji=':('):
    print(last_word, emoji)


hello()
bye('Bye bye')
hello_with_greeting('Hello parameter')


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()