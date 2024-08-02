## Best practice to name variable
# 1/ snake_case
# 2/ Start with lowercase or underscore
# 3/ Letters, numbers, underscores
# 4/ Case sensitive
# 5/ Don't overwrite keyword
# Note: _ indicates private variables in Python

### constants == best practice capital all word
### __ == double underscore indicates dunders (i.e. also called magic methods because they allow Python classes to emulate built-in types and perform various operations, such as object initialization, comparison, and iteration.)
### list of dunder methods : https://www.geeksforgeeks.org/dunder-magic-methods-python/

a,b,c = 1,2,3
print(a)
print(b)
print(c)