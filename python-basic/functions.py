# def -> define
# can add parameter to function
# positional parameter - because position is important
def say_hello(name, emoji):
    print(f'Hello {name} {emoji}')


#arguments
# positional arguments - arguments that require in correct position
say_hello('DEF', ':)')

# argument - actual value used to pass in to the function
# parameter - name of variables that we receive in the function

# keyword arguments - tell function explicit what are the values of the parameters
say_hello(emoji=':)', name='XYZ')


# Default parameters - give default values to the function of there aren't no input value
def say_hello_default(name='DEF', emoji=':))'):
    print(f'Hello {name} {emoji}')


say_hello_default('ABC', '()')
say_hello_default('Time')


## for function -> if there are no return statement, it will return None
def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))


## Function Rule of thumb
# Function should do something really well
# Should return something
