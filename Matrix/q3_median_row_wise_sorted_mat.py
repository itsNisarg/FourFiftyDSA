# Given a row-wise sorted matrix mat[][] of size n x m, where the number of rows and columns is always odd. Return the median of the matrix.


def median(self, mat):
    from bisect import bisect_right

    # code here
    n, m = len(mat), len(mat[0])
    if 1 == m and n == 1:
        return mat[0][0]

    median_pos = (n * m + 1) // 2       # Do n*m + 1 to handle the case when n*m is odd. Then divide by 2 to get the median position

    low, high = mat[0][0], mat[0][-1]
    for row in mat:
        low = min(low, row[0])
        high = max(high, row[-1])

    while low < high:   # Don't use low <= high because we want to find the first element that is greater than or equal to the median position
        middle = low + (high - low) // 2
        pos_mid = 0
        for row in mat:
            pos_mid += bisect_right(row, middle) # Do bisect_right to get the number of elements less than or equal to middle in the current row
        if pos_mid < median_pos:    # Don't use pos_mid <= median_pos because we want to find the first element that is greater than or equal to the median position
            low = middle + 1    # Move low to middle + 1 because we want to find the first element that is greater than or equal to the median position
        else:
            high = middle   # Don't use high = middle - 1 because we want to find the first element that is greater than or equal to the median position
    return low  # Return low because it is the first element that is greater than or equal to the median position
