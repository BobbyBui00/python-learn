def check_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


name = input(str('Enter a string: '))
is_palindrome = check_palindrome(name)
print(is_palindrome)
