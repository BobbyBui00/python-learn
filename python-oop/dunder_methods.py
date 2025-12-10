# Dunder methods are methods that are denoted with __<method_name>__

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')

    def __call__(self):
        print('YES??')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(dir(action_figure))
print(action_figure.__str__())
print(str(action_figure))
print(action_figure)

print(action_figure.__len__())
print(len(action_figure))

action_figure.__del__()

action_figure.__call__()
print(action_figure())

print(action_figure['name'])
print(action_figure['has_pets'])
