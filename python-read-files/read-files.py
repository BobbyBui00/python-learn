# my_file = open('text.txt')
# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())
# print(my_file.readlines())
#
# ## Best practice, close the file after finishing up
# my_file.close()

## Mode: ['r', 'w', 'r+' - if we want both read and write, 'a' - append at the end of the file]
## when we open the file, the cursor reset, it will always start at the begining of the file
# with open('text.txt', mode='a') as my_file:
#     text = my_file.write("Hey! it\'s me!")
#     print(text)

## Create a file that doesn't exist.
with open('test-without-app.txt', mode='w') as my_file:
    text = my_file.write("Hi, created from python")
    print(text)

## REad file from different location
with open('app/test.txt', mode='r') as my_file:
    # text = my_file.write("Hi, created from python")
    print(my_file.readlines())

# OR
with open('C:\workspaces\python-workspace\python-learning\python-read-files\\app\\test.txt', mode='r') as my_file:
    # text = my_file.write("Hi, created from python")
    print(my_file.readlines())

## Common error when work with file
try:
    with open('text.txt', mode='a') as my_file:
        text = my_file.write("Hey! it\'s me!")
        print(text)
except FileNotFoundError:
    print('Couldnt found the file')
except IOError as e:
    raise e