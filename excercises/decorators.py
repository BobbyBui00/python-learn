# Create an @authenticated decorator that only allows the function to run it user1 has 'valid' set to True:

user1 = {
    'name': 'Sorna',
    'valid': True  # Changing this will either run or not run the message_friends function
}


def authenticate(fn):
    def wrapper(*args, **kwargs):
        for user in args:
            if 'valid' in user and user['valid']:
                fn(*args, **kwargs)
            else:
                print("User doesn't not allow to run this function")

    return wrapper


@authenticate
def message_friends(user):
    print('Message has been sent')


message_friends(user1)
