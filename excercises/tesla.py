# age = input('What is your age?: ')
#
# if int(age) < 18:
#     print('Sorry, you are too young to drive this car. Powering off')
# elif int(age) > 18:
#     print('Powering on. Enjoy your ride!')
# elif int(age) == 18:
#     print('Congratulations on your first year of driving. Enjoy your ride!')

# 1: Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get promtped for age
# 2: Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering on, Enjoy your ride!"
# Also make it so that the default age is set to 0 if no argument is given

def checkDriverAge():
    age = input('What is your age?: ')

    if int(age) < 18:
        print('Sorry, you are too young to drive this car. Powering off')
    elif int(age) > 18:
        print('Powering on. Enjoy your ride!')
    elif int(age) == 18:
        print('Congratulations on your first year of driving. Enjoy your ride!')


def checkDriverAgeWithParameter(age_1=0):
    if age_1 < 18:
        print('Sorry, you are too young to drive this car. Powering off')
    elif age_1 > 18:
        print('Powering on. Enjoy your ride!')
    elif age_1 == 18:
        print('Congratulations on your first year of driving. Enjoy your ride!')


if __name__ == '__main__':
    selection = int(input('Select 1 or 2: '))
    if selection == 1:
        checkDriverAge()
    else:
        age = input('What is your age?: ')
        checkDriverAgeWithParameter(int(age)) if age != '' else checkDriverAgeWithParameter()

