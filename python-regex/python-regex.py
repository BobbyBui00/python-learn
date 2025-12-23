import re

pattern = re.compile(r"([a-zA-Z]).([a])") ## r before the regex to denote that this is the raw string, ignore any special characters
string = 'search this inside of this text please!'

a = pattern.search(string)
print(f'a: {a.span()}')
print(f'a: {a.start()}')
print(f'a: {a.end()}')
print(f'a: {a.group()}')
b = pattern.findall(string)
print(f'b: {b}')

c = pattern.fullmatch(string) ## in order to the full match to return, the full string has to be exactly the same
print(f'c: {c}')

d = pattern.match(string)
print(f'd: {d}')


