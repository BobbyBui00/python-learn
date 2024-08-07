quote = 'to be or not to be'

print(quote[0:len(quote)])

print('Upper method: ' + quote.upper())
print('Capitalize method: ' + quote.capitalize())
print('Lower method: ' + quote.lower())
print('Find word be: ' + str(quote.find('be')))
print('Replace be with me method', quote.replace('be', 'me'))

print(quote) ## -> string is immutable, with all conversion above, it will create new instance not modify the existing one


