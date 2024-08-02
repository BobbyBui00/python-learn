# operator precedence
print(20 + 3 * 4)
print((20 - 3) + 2 ** 2)

## order
## 1/ ()
## 2/ **
## * and /
## + and -

print((5 + 4) * 10 / 2) #45

print(((5 + 4) * 10) / 2) #45

print((5 + 4) * (10 / 2)) #45

print(5 + (4 * 10) / 2) #25

print(5 + 4 * 10 // 2) #5


## augmented assignment operator
value = 5
value = value + 2
print(value)
value += 3
print(value)
value -= 3
print(value)
value *= 3
print(value)
value /= 3
print(value)