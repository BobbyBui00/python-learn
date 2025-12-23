## Debugging

# Best practice for easily debugging
#     1/ linting
#     2/ recommend use IDE/Editor
#     3/ read errors
#     4/ pdb - python debugger

import pdb

def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2

add(4, 5)