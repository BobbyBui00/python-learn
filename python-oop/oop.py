## OOP : Object Orient Programing - paradigm

### CLASS

class PlayerCharacter:
    ## Class object attribute -> not dynamic
    membership = True

    ## __init__ : dunder method or magic method or CONSTRUCTOR
    ## name in this case is a parameter and it is mandatory when instantiate an object
    ## self : refer to the class it is in (in this case it is PlayerCharacter
    def __init__(self, name='anonymous', age=0):
        # if self.membership: ## OR PlayCharacter.membership
        if age > 18:
            ## regular object attribute -> dynamic
            self.name = name
            self.age = age

    def run(self):
        print('Run!!')
        return 'done'

    def shout(self):
        print(
            f'My name is {self.name}')  ## Cannot do PlayerCharacter.name because the name attribute is not a Class Object attribute.


player1 = PlayerCharacter('Allan', 25)
player2 = PlayerCharacter('Tom', 35)
# player3 = PlayerCharacter('Cat', 10)
player2.attack = 50

# print(f'{player1.name} + {player1.age} + {player1.run()} + {player1.attack}')
print(f'{player2.name} + {player2.age} + {player2.run()} + {player2.attack}')

# help(list) ->> return the 'blueprint' all the method and attribute of the class

print(player1.membership)
print(player2.membership)
# print(player3.membership)

player1.shout()
player2.shout()
# player3.shout()


# User:
#  - Wizard
#  - Archers
#  - Duck

class User: # behind the scene, the User class take object class as its inheritance User(object)

    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows left - {self.num_arrows}')



wizard1 = Wizard('Bobby', 100)
archer1 = Archer('Robin', 50)
wizard1.attack()
wizard1.sign_in()
archer1.attack()
archer1.sign_in()

print(isinstance(archer1, Archer)) # True
print(isinstance(archer1, Wizard)) # False
print(isinstance(archer1, User)) # True
print(isinstance(archer1, object)) # True - Because in Python every custom class are from the object base class

for char in [wizard1, archer1]:
    char.attack()


#### SUPER class

class User1: # behind the scene, the User class take object class as its inheritance User(object)

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class WizardSuper(User1):
    def __init__(self, name, power, email):
        # super().__init__(email) ## refer to User1 which has the __init__ email
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class ArcherSuper(User1):
    def __init__(self, name, num_arrows, email):
        # super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'Attacking with arrows left - {self.num_arrows}')

    def run(self):
        print('Ran really fast')

class HybridBorg(WizardSuper, ArcherSuper): ## multiple inheritance
    def __init__(self, name, power, arrows, email):
        ArcherSuper.__init__(self, name, arrows, email)
        WizardSuper.__init__(self, name, power, email)



super_wizard = WizardSuper('Robin', 10, 'abc@gmail.com')
# print(super_wizard.email)

## introspection - in computer programming means the ability to determine the type of an object at a runtime
print(dir(super_wizard))


hb1 = HybridBorg('borgie', 50, 10, 'abc@gmail.com')
hb1.run()
hb1.attack()
hb1.check_arrows()
hb1.attack()
hb1.sign_in()