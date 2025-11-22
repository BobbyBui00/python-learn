## OOP : Object Orient Programing - paradigm

### CLASS

class PlayerCharacter:
    ## Class object attribute -> not dynamic
    membership = True

    ## __init__ : dunder method or magic method or CONSTRUCTOR
    ## name in this case is a parameter and it is mandatory when instantiate an object
    ## self : refer to the class it is in (in this case it is PlayerCharacter
    def __init__(self, name = 'anonymous', age = 0):
        # if self.membership: ## OR PlayCharacter.membership
        if age > 18:
            ## regular object attribute -> dynamic
            self.name = name
            self.age = age

    def run(self):
        print('Run!!')
        return 'done'

    def shout(self):
        print(f'My name is {self.name}') ## Cannot do PlayerCharacter.name because the name attribute is not a Class Object attribute.


player1 = PlayerCharacter('Allan', 25)
player2 = PlayerCharacter('Tom', 35)
player3 = PlayerCharacter('Cat', 10)
player2.attack = 50

# print(f'{player1.name} + {player1.age} + {player1.run()} + {player1.attack}')
print(f'{player2.name} + {player2.age} + {player2.run()} + {player2.attack}')

# help(list) ->> return the 'blueprint' all the method and attribute of the class

print(player1.membership)
print(player2.membership)

player1.shout()
player2.shout()
player3.shout()
