### INT & FLOAT DATA TYPE

print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)

## Check data type
print(type(2 + 4)) 
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))

print(2 ** 2) ## ** === square
print(5 // 4) ## // === divide and round down the answer
print(5 % 4)

# Math Functions
print(round(3.9)) ## round up if the decimal larger or equal than 5, round down if the decimal smaller than 5
print(abs(-20)) ## Absolute

### COMPLEX DATA TYPE
# Beside int, float -> third type of data type is "Complex"

print(bin(5)) # Return binary of a value ->> 0b101 : 0b represent binary number in Python, 101 is actual binary of 5
print(int("0b101", 2)) # Return integer value of a binary number ->> 5 : 2 represent 0 and 1

#print(bin(10.5)) # bin() only used for Integer


### STR DATA TYPE
'hi hello there' ## or "hi hello there! "

print(type('hi hello there'))
username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
THIS IS A VERY LONG STRING
ON THE THIRD LINE
'''

print(long_string)

# string concatenation
print('hello' + ' Allan')
# str cannot concat integer

### Type Conversion
print(type(str(100))) # -> type str
print(type(int(str(500)))) # -> type int

### BOOLEAN DATA TYPE
# bool either True or False

name = 'Allan'
is_cool = False

is_cool = True

print(f'{name} profile is cool? {is_cool}')
print(bool(1))
print(bool(0))
print(bool('True'))
print(bool('False'))