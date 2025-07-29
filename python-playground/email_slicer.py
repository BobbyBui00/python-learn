email = str(input("Enter your email: "))

username = email.split("@")[0]
domain = email.split("@")[1]

### OR ###

username1 = email[:email.index("@")]
domain1 = email[email.index("@") + 1:]

print(f"Your user name is '{username}' and you domain is '{domain}'")

### OR ###

print("Your user name is '{}' and you domain is '{}'".format(username1, domain1))
