list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 2, 2.4, 'a', 'b', True, False]

### LIST SLICING
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart)
print(amazon_cart[0::2]) # Similar to String Slicing
print(amazon_cart[0])
print(amazon_cart[1])


amazon_cart[0] = 'laptop' ## Unlike string which is immutable, list is mutable

new_cart = amazon_cart ## create new_cart list pointing to the same in-memory location with amazon_cart. Which means , if there are modifications with new_cart or amazon_cart list, the other list is affected.
new_cart[0] = 'gums'
print(new_cart) ## ['gums', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) ## ['gums', 'sunglasses', 'toys', 'grapes']

new_cart1  = amazon_cart[:] ## create new_cart1 list as a copy of amazon_cart. They are two different lists having different in-memory location. Modify one list does not affect the other list
new_cart[0] = 'phones'
print(new_cart1) ## ['phones', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) ## ['gums', 'sunglasses', 'toys', 'grapes']


### MATRIX

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1]) # [2]


### LIST METHODS

basket = [1, 2, 3, 4, 5]
print(len(basket)) ### 5

# append()
new_list = basket.append(True)
print(basket) ## [1, 2, 3, 4, 5, True]
print(new_list) ## None - because append change the list in place, does not return new list

# insert()
basket.insert(4, 100)
print(basket) ## [1, 2, 3, 4, 100, 5, True]

# extend()
new_list = basket.extend([100, 101])
print(basket) ## [1, 2, 3, 4, 100, 5, True, 100, 101]
print(new_list)

# pop()
basket.pop()
print(basket) ## [1, 2, 3, 4, 100, 5, True, 100]
basket.pop(0)
print(basket) ## [2, 3, 4, 100, 5, True, 100]
new_list = basket.pop(5)
print(new_list) ## True

# remove()
basket.remove(4)
print(basket) ## [2, 3, 100, 5, 100]

# clear()
basket.clear()
print(basket) ## []

list_arr = ['a', 'b', 'c', 'd', 'e']

# index()
print(list_arr.index('b')) # 1
print(list_arr.index('d', 0, 4)) # 3
# print(list_arr.index('d', 0, 1)) # Value Error: element is not in list

# in
print('b' in list_arr) # True
print('x' in list_arr) # False

# count()
print(list_arr.count('b')) # 1
list_arr.append('b')
print(list_arr.count('b')) # 2

# sort()
list_arr.sort()
print(list_arr) # ['a', 'b', 'b', 'c', 'd', 'e']

# sorted
list_arr.append('a')
print(sorted(list_arr)) # ['a', 'a', 'b', 'b', 'c', 'd', 'e']
print(list_arr) # ['a', 'b', 'b', 'c', 'd', 'e', 'a']
### Note: sorted() and sort() both sort the list but sorted() will return a new sorted list and does not modify existing list. sort() will modify existing list and not return new list

# reverse()
list_arr.reverse()
print(list_arr) # ['a', 'e', 'd', 'c', 'b', 'b', 'a']

# range()
print(list(range(1, 100)))
print(list(range(100)))

# .join()
sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence) # hi!my!name!is!JOJO

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence) # hi my name is JOJO

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence) # hi my name is JOJO

### LIST UNPACKING
a,b,c = [1,2,3]

print(a) # 1
print(b) # 2
print(c) # 3

a,b,c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4, 5, 6, 7, 8]
print(d) # 9