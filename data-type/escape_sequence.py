### ESCAPE SEQUENCE
weather = 'It\'s sunny'
print(weather)

weather1 = ('It\'s \"kind of\" sunny')
print(weather1)

print('It\'s \"kind of\" sunny \n Hope you have a good day!')

# \t : Tab
# \n : new line


### FORMATTED STRINGS

name = input('What is your name? ')
age = int(input('How old are you? '))
print(f'Hi {name}. You are {age} years old') # Only available for Python >= 3
print('Hi {}. You are {} years old'.format(name, age)) # Python >= 2
print('Hi {1}. You are {0} years old'.format(name, age)) # Python >= 2
print('Hi {new_name}. You are {age} years old'.format(new_name='Sally', age=100)) # Python >= 2
print('Hi %s. You are %d years old' % (name, age))
print('Hi %(last)s, %(first)s %(last)s' % { 'first': "James", 'last': "Bond" })


### STRING INDEXES
selfish = 'me me me'
print(selfish[0])

### [start:stop]
print(selfish[0:2])

### [start:stop:stepover]
print(selfish[0:8:2])

### [start:]
print(selfish[1:])

### [:stop]
print(selfish[:5])

### [::stepover]
print(selfish[::1])

print(selfish[-1]) # get the last element, in Python negative index represent backward order

print(selfish[::-1]) # reverse the string
