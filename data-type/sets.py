# Sets are simple unordered collections of unique ojects

my_set = { 1, 2, 3, 4, 5, 6 }
print(my_set) # -> { 1, 2, 3, 4, 5, 6 }

my_set1 = { 1, 2, 3, 4, 5, 6, 6 }
print(my_set1) # -> { 1, 2, 3, 4, 5, 6 } -> even though 6 appears twice in my_set1, it will return one 6 because set only return unique sets or unique items

my_set.add(100)
my_set.add(6)
print(my_set) # -> { 1, 2, 3, 4, 5, 6, 100 }


# Exercise: Given my_list = [1, 2, 3, 4, 5, 5], convert to set and remove duplicate if needed
my_list = [1, 2, 3, 4, 5, 5]

## Junior code
my_set2 = set()
for i in my_list:
    my_set2.add(i)
print(f"Junior code {my_set2}")

## senior code
print(f"Senior code {set(my_list)}")

# print(my_set2[0]) -> TypeError -> set doesn't support indexing
print(1 in my_set2) # -> check if 1 exists
print(len(my_set2))
print(list(my_set2)) # -> convert back to list

new_set = my_set2.copy()
print(my_set2.clear()) # -> set(), empty set
print(new_set) # -> { 1, 2, 3, 4, 5 }


### SET METHODS

my_set = { 1, 2, 3, 4, 5 }
your_set = { 4, 5, 6, 7, 8, 9, 10 }

# .difference() - return a new set with elements in the first set that are not in the second set
print(my_set.difference(your_set))  # -> { 1, 2, 3 }

# .discard() - remove an element from a set if it is a member
my_set.discard(5)
print(my_set) # -> { 1, 2, 3, 4 }
print(my_set.discard(5)) # -> None

# .difference_update() - remove all elements of another set from this set
print(my_set.difference_update(your_set)) # None
my_set.difference_update(your_set)
print(my_set) # -> { 1, 2, 3 }

# .intersection() - tell where this list intersect with other list
my_set = { 1, 2, 3, 4, 5 }
your_set = { 4, 5, 6, 7, 8, 9, 10 }
print(my_set.intersection(your_set)) # ->  { 4, 5 }
print(my_set & your_set) # -> { 4, 5 }

# .isdisjoint() - check if two lists contains same element(s), return False is two lists contain same element(s), True if two lists are not overlapping
print(my_set.isdisjoint(your_set)) # -> False

# .issubset() -  check if one list is a subset of other list. return True is ENTIRE set is in your list
my_set1 = { 4, 5 }
your_set = { 4, 5, 6, 7, 8, 9, 10 }
print(my_set1.issubset(your_set)) # -> True
print(your_set.issubset(my_set1)) # -> False

# .issuperset() - Check if the list contains ALL ELEMENTS of other lists
print(my_set1.issuperset(your_set)) # -> False
print(your_set.issuperset(my_set1)) # -> True

# .union() - combine two lists remove duplicates if exists, RETURN A NEW SET
my_set.union(your_set)
print(my_set) # -> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
print(my_set | your_set) # -> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }



