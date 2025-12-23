##  ERROR HANDLING   ##
#
# try:
#     do_something_here
# except:
#     catch the exception
# else:
#      if there is any errors, catch in the exception block, else continue here
# finally:
#      return everytime regardless successful or failed

# or
# raise custom exception with raise keyword

while True:
    try:
        age = int(input('What is your age: '))
        # print(age)
        10 / age
    except ValueError as e:
        print('Please enter a number')
    except ZeroDivisionError as e:
        print('Please enter an age larger than 0 ')
    else:
        print('Thank you')
        break
    finally:
        print('Ok, I am finally done')

## Error Handling
def sum(num1, num2):
    try:
        return num1 / num2
    # Best practice: Catch the exception as accurate as possible
    # Exceptions can be grouped together
    except (TypeError, ZeroDivisionError) as e:
        print(f'Please enter a valid numbers: {e}')

print(sum(1, 0))
print(sum(1, '2'))
