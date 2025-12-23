from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

## Counter the number of character/element in the array
li = [1, 2, 3, 4, 5, 6, 7, 7]
sentences = 'blah blah blah. Thinking about Python!'
print(Counter(sentences))

## return the default value if the element is not exist
dictionary = defaultdict(lambda: 'Does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])

## OrderedDict - retain an order of element you inserted. Regularl dictionary doesn't have any sense of order.
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

d = {'c': 100}
d['a'] = 1
d['b'] = 2

d2 = {'c': 100}
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

#### datetime   ###
print(datetime.time())
print(datetime.time(5, 24, 1))
print(datetime.date.today())


#### array      ###
arr = array('i', [1, 2, 3])
print(arr[0])

