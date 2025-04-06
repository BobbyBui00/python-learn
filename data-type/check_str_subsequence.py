str1 = 'adg'
str2 = 'abcgefdhi'


def check_subsequence(self, sub_str, big_str):
    i = j = 0

    while i < len(sub_str) and j < len(big_str):
        if sub_str[i] == big_str[j]:
            i += 1
        j += 1

    return i == len(sub_str)


print(check_subsequence(str1, str2))