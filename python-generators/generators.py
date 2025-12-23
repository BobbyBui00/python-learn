## A generators is a special type of thing in Python that allows us to use a special keyword called yield and it can pause and resume functions
## iterable is any object in Python which we are able to loop through. Under the hood, it has the dunder method. __iter__
## iteration is an art/process of taking the value iterated and do something
## generators is iterable but not everything iterable is a generators. Generator is an subset of iterable
## if a function as a yeild keyword, it becomes a generator, what it does, it keeps the value in current value in memory
## you can get a StopIteration if the exceed the item in the range

range(100)
list(range(100))


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result
#
#
# my_list = make_list(100)
# print(my_list)


def generator_function(num):
    for i in range(num):
        yield i * 2


## yield pauses the function and come back to it when we do something to it, which is called next

# for item in generator_function(1000):
#     print(item)

g = generator_function(100)
print(g)
print(next(g))
next(g)
next(g)
print(next(g))


def special_for_loop(iterable):
    iterator = iter(iterable)  ## allow us to use the next function for iterable
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


special_for_loop([1, 2, 3])


## Explaining how the Range generator works under the hood
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)
