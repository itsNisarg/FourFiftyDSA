# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Note: You need to solve this problem without utilizing the built-in sort function.

# Count the number of 0s, 1s and 2s and place them in the array
# We don't need to count the number of 2s as they shall be n-0s-1s
# O(2n)


def method_1(arr):
    zeroes, ones = 0, 0

    for n in arr:
        if n == 0:
            zeroes += 1
        if n == 1:
            ones += 1

    i = 0

    while i < zeroes:
        arr[i] = 0
        i += 1

    while i < zeroes + ones:
        arr[i] = 1
        i += 1

    while i < len(arr):
        arr[i] = 2
        i += 1

    return arr


# Method 2: Use Dutch National Flag Algo by using 3 pointers
# [0, lo-1] => 0
# [lo, mid-1] => 1
# [mid, hi] => Unknown
# [hi+1, n-1] => 2


def method_2(arr):
    lo, mid, hi = 0, 0, len(arr) - 1

    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr


if __name__ == "__main__":
    print(method_2([0, 1, 2, 0, 1, 2, 0, 1, 2, 2, 1, 0]))
