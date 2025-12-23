import sys
import random


def main():
    random_num = random.randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            user_num = int(input('Enter a random number from 1 to 10: '))
            if user_num < 0 or user_num > 10:
                raise IOError('Please enter value from 1 to 10')
            elif 0 < user_num < 10 and user_num == random_num:
                print('You are correctly!')
                break
        except (TypeError, ValueError) as e:
            print(f'Error: {e}. Please enter a number')
        except Exception as e:
            print(f'Unexpected error: {e}')


if __name__ == '__main__':
    main()
