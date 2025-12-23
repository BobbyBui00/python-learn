import utility
# from utility import * // import all of the functions contained inside the utility
from packages.more_shopping.shopping_cart import buy
import random
# import random as rd ## give it an alias
import sys

print(utility.multiply(2, 3))
print(utility.divide(5, 2))
print(buy('Car'))
print(max([1, 2, 3]))
print(utility.max())
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))

my_list = [1, 2, 3, 4, 5]
print(random.shuffle(my_list))
print(my_list)

sys.argv ## accept parameter(s) given when run the python file

