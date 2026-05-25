# Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Examples:

# Input: arr[] = [1, 4, 3, 2, 6, 5]
# Output:  [5, 6, 2, 3, 4, 1]
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

# Input: arr[] = [4, 5, 1, 2]
# Output: [2, 1, 5, 4]
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.


## Method 1: Python Function reverse()


def method_1(arr):
    return arr.reverse()


## Method 2: Extra Space O(n)


def method_2(arr):
    n = len(arr)
    reverse_arr = [None] * n
    for i in range(n):
        reverse_arr[i] = arr[n - i - 1]
    return reverse_arr


## Method 3: Extra Space O(1)


def method_3(arr):
    tmp = None
    n = len(arr)
    for i in range(n // 2):
        tmp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = tmp
    return arr


## Method 4: Two Pointers


def method_4(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left] = arr[left] ^ arr[right]  # Swap without extra space (only int allowed)
        arr[right] = arr[left] ^ arr[right]
        arr[left] = arr[left] ^ arr[right]

        left += 1
        right -= 1

    return arr


## Method 5: Single Pointer


def method_5(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr
