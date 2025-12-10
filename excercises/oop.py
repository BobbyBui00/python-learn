class Cat1:
    species = 'mammal'
    oldest = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return max(self.age, other.age)


## 1 Instantiate the Cat object with 3 cats
cat2 = Cat1('def', 20)
cat1 = Cat1('abc', 10)
cat3 = Cat1('ghi', 30)


## 2 Create a function that finds the oldest cat
def oldest(*args):
    oldest_age = max(args)
    print(f'The oldest cat is {oldest_age} years old')


## 3 Print out: 'The oldest cat is x years old'. x will be the oldest cat age by using the function in #2
oldest(cat1.age, cat2.age, cat3.age)
print(f'The oldest cat is {cat1 == cat2 == cat3} years old')


#### OOP Exercise

class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around!'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1. Add another Cat
class Happy(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2. Create a list of all of the pets (create 3 cat instances from the above)
happy1 = Happy('1', 10)
happy2 = Happy('2', 15)
happy3 = Happy('3', 20)

my_cats = [happy1, happy2, happy3]

# 3. Instantiate the Pet class with all of your cats use variable my_pets
my_pets = Pets(my_cats)

# 4. Output all of the cats walking using the my_pets instance
my_pets.walk()