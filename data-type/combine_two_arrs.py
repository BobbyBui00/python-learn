arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]


def merge_two_arrays(array1, array2):
    final_arr = []
    n = m = 0

    while n < len(array1) and m < len(array2):
        if array1[n] < array2[m]:
            final_arr.append(array1[n])
            n += 1
        else:
            final_arr.append(array2[m])
            m += 1

    while n < len(array1):
        final_arr.append(array1[n])
        n += 1

    while m < len(array2):
        final_arr.append(array2[m])
        m += 1

    return final_arr


print(merge_two_arrays(arr1, arr2))