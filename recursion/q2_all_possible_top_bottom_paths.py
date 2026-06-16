# Given a n x m matrix mat[][]. Your task is to find and return all possible paths from the top-left cell (0, 0) to the bottom-right cell (n-1, m-1).

# From each cell, you can move only in the following two directions:

# Right → (i, j+1)

# Down → (i+1, j)

# Return all possible paths, where each path is represented as a list of matrix elements encountered along the path.


class Solution:
    def findAllPossiblePaths(
        self, n: int, m: int, mat: list[list[int]]
    ) -> list[list[int]]:
        paths = []
        path = [mat[0][0]]
        self.find_paths(mat, paths, path, 0, 0)
        return paths

    def find_paths(self, mat, paths, path, r, c):
        if r == len(mat) - 1 and c == len(mat[0]) - 1:
            paths.append(path)
            return

        if r < len(mat) - 1:
            self.find_paths(mat, paths, path + [mat[r + 1][c]], r + 1, c)
        if c < len(mat[0]) - 1:
            self.find_paths(mat, paths, path + [mat[r][c + 1]], r, c + 1)
