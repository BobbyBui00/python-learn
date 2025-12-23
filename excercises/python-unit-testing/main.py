import random
import sys


def main():
    random_num = random.randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            user_num = int(input('Enter a random number from 1 to 10: '))
            if compare(random_num, user_num):
                break
        except (TypeError, ValueError) as e:
            print(f'Error: {e}. Please enter a number')
        except Exception as e:
            print(f'Unexpected error: {e}')


def compare(computer_guess, user_guess):
    if user_guess < 0 or user_guess > 10:
        raise IOError('Please enter value from 1 to 10')
    elif 0 < user_guess < 10 and user_guess == computer_guess:
        print('You are correctly!')
        return True


if __name__ == '__main__':
    main()
