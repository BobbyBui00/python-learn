name = input('Enter username: ')
password = input('Enter password: ')

print(f'{name}, your password {'*' * len(password)} is {len(password)} letters long')