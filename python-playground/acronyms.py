user_input = str(input("Enter a phrase: "))

phrases = user_input.split()
a = ""

for i in phrases:
    a = a + i[0].upper()

print(a)
