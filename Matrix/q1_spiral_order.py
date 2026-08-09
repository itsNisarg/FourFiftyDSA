# Given a rectangular matrix mat[][] of size n x m, and return a 1D array containing all its elements in spiral order.


def method_1(mat):
    if not mat:
        return []

    res = []
    top, bottom, left, right = 0, len(mat) - 1, 0, len(mat[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for j in range(left, right + 1):
            res.append(mat[top][j])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            res.append(mat[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for j in range(right, left - 1, -1):
                res.append(mat[bottom][j])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                res.append(mat[i][left])
            left += 1

    return res


def method_2(mat):
    ans = []
    n, m = len(mat), len(mat[0])

    layers = (min(n, m) + 1) // 2

    for layer in range(layers):
        for j in range(layer, m - layer):
            ans.append(mat[layer][j])

        if layer == n - layer - 1:
            break

        for i in range(layer + 1, n - layer):
            ans.append(mat[i][m - layer - 1])

        if layer == m - layer - 1:
            break

        for j in range(m - layer - 2, layer - 1, -1):
            ans.append(mat[n - layer - 1][j])

        for i in range(n - layer - 2, layer, -1):
            ans.append(mat[i][layer])

    return ans
