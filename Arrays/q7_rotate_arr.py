# Given an array arr, rotate the array by one position in clockwise direction.


def method_1(arr):
    last = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last
    return arr


def method_2(arr):
    temp = arr[-1]
    arr[1:] = arr[:-1]
    arr[0] = temp
    return arr
