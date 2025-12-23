# At least 8 characters long
# Can contains any sort of letter, number, and $%#@
# End with a number

import re


def main():
    pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}[0-9]$")
    password = str(input('Enter your password: '))
    if not pattern.match(password):
        raise Exception('Invalid password')
    else:
        print('Valid password')


if __name__ == '__main__':
    main()
