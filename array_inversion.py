a = [4, 3, 2, 1]


def array_inversion(arr):
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


count_invert = array_inversion(a)
print(count_invert)
