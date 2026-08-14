# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


def rotate(self, matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n, m = len(matrix), len(matrix[0])
    for i in range(0, n - 1):
        for j in range(i + 1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(i, j)

    for j in range(m // 2):
        for i in range(n):
            matrix[i][j], matrix[i][m - j - 1] = matrix[i][m - j - 1], matrix[i][j]
