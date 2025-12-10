##OOP

# private variable - best practice naming convention _<variable_name>

class PlayerCharacter:
    membership = True
    # _privateVariable

    # Dunder method __<function_name>__ - also a convention to let the coder know you shouldn't use this naming convention
    def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    # For classmethod, the first argument is usually cls = class
    # It is different from other method because you can use it without initiating a class similar to statis method in Java
    @classmethod
    def adding_thing_class_method(cls, num1, num2):
        # One of the usage of this is you can initiate a class within the classmethod using cls
        # Usage: we use it when we care about the class state or when you want to change attribute
        return cls('Teddy', num1 + num2)
        # return num1 + num2

    @staticmethod
    def adding_thing_static_method(num1, num2):
        # exactly the same as classmethod but the difference is you don't have access to the cls (class) object like classmethod
        # Therefore, you cant initiate a class like in @classmethod
        # Usage: we would use a @staticmethod when we dont care about the class state
        return num1 + num2


player1 = PlayerCharacter('Tom', 20)
print(player1.adding_thing_class_method(2, 3))
player3 = PlayerCharacter.adding_thing_class_method(5, 10)
print(player3.age)
print(PlayerCharacter.adding_thing_static_method(10, 10))