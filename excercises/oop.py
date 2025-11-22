class Cat:
    species = 'mammal'
    oldest = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return max(self.age, other.age)


## 1 Instantiate the Cat object with 3 cats
cat2 = Cat('def', 20)
cat1 = Cat('abc', 10)
cat3 = Cat('ghi', 30)


## 2 Create a function that finds the oldest cat
def oldest(*args):
    oldest_age = max(args)
    print(f'The oldest cat is {oldest_age} years old')


## 3 Print out: 'The oldest cat is x years old'. x will be the oldest cat age by using the function in #2
oldest(cat1.age, cat2.age, cat3.age)
print(f'The oldest cat is {cat1 == cat2 == cat3} years old')
