# You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.


def rowWithMax1s(self, arr):
    from bisect import bisect_right

    # code here
    max_ones = 0
    ans = -1
    for i, row in enumerate(arr):
        ones = len(row) - bisect_right(row, 0)
        if ones > max_ones:
            ans = i
            max_ones = ones
    return ans


def method_2(arr):
    # code here
    ans = -1
    ver, hor = 0, len(arr[0]) - 1
    while hor >= 0 and ver < len(arr):
        if arr[ver][hor] == 1:
            ans = ver
            hor -= 1
        else:
            ver += 1
    return ans
