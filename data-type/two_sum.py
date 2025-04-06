sorted_array = [1, 2, 4, 6, 8, 9, 14, 15]


def check_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return list((arr[left], arr[right]))
        elif curr_sum > target:
            right -= 1
        else:
            left += 1

    return None


num = int(input('Enter number: '))
results = check_sum(sorted_array, num)
print(results)
