is_old = True
is_licensed = True

# if <condition>
if is_old:
    print("You are old enough to drive!")
elif is_licensed:
    print("You can drive!")
else:
    print("You cannot drive!")


if is_old and is_licensed:
    print("You are old enough to drive, and you have a license!")
else:
    print("You cannot drive!")


print("Come here")

## Truthy and Falsy
# Underneath, the if statement convert the value to boolean by bool(). For none boolean type, it does conversion to boolean and evaluate the condition

password = "123"
username = 'johnny'

if password and username:
    print("User provides all information")


### TERNARY OPERATOR

# Syntax: <condition_if_true> if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)


### SHORT CIRCUITING
is_friend = True
is_user = False

print(is_friend and is_user) # -> False
print(is_friend or is_user) # -> True


#### LOGICAL OPERATORS
# List of logical operators:
# >
# <
# ==
# !=
# <=
# >=
# and
# or
# not
print(ord('a')) # -> convert value to ascii value
print(ord('A')) # -> convert value to ascii value
print(1 < 2 < 3 < 4 < 5) # -> True
print(1 < 2 > 3 < 4 < 5) # -> False
print(not True)
print(not(True))



