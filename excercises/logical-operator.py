is_magician = False
is_expert = True

## check if magician AND expert: "You are a master magician"
## check if magician but not expert: "At least you're getting there"
## check if not magician: "You need magic powers"

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you're getting there")
else:
    print("You need magic powers")


## == check for equality or equality of value
print(True == 1) ## True --> True == bool(1) -> True == True
print('' == 1) ## False --> Empty string is falsy
print([] == 1) ## False --> Empty array is falsy
print(10 == 10.0) ## True --> Convert int to float
print([] == []) ## True -->
print('1' == 1) ## False --> bad code

## is check for the location of memory if they are pointing to the same location
## for data structure like array, dictionaries, sets, tuples, when we create a new data structure, it assigns new location in memory
print(True is 1) ## False
print('' is 1) ## False
print([] is 1) ## False
print(10 is 10.0) ## False
print([] is []) ## False
print('1' is 1) ## False
print(True is True) ## True
print('1' is '1') ## True
print(10 is 10) ## True


