nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8


def find_longest_sub_arr(arr, target):
    left = curr = ans = 0

    for right in range(len(arr)):
        curr += arr[right]
        while curr > target:
            curr -= arr[left]
            left += 1
        ans = max(ans, right - left + 1)

    return ans


print(find_longest_sub_arr(nums, k))
