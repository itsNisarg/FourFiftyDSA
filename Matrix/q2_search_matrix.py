# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


def searchMatrix(self, mat, target: int) -> bool:
    n, m = len(mat), len(mat[0])
    left = -1
    right = n * m
    jump = right // 2 + 1
    # Intuitive Binary Search
    while jump > 0:
        while ((ind := left + jump) < right) and (mat[ind // m][ind % m] <= target):
            left += jump
        jump = jump // 2
    return mat[left // m][left % m] == target
