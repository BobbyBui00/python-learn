i = 0
while i < 50:
    print(i)
    i += 1

while 0 < 50:
    print(0)
    break

## else runs if the condition is false and while is exit
## else only runs if there is no break inside the while block, if there is a break, exit the while loop and continue with the work after and not going into else
j = 0
while j < 50:
    print(j)
    j += 1
else:
    print('Done with all the work!')

while True:
    response = input('Say something: ')
    if response == 'bye':
        break
