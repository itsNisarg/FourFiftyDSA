# Given a binary matrix maze[][] of size n × n containing values 0 and 1, find all possible paths for a rat to travel from the source cell (0, 0) to the destination cell (n - 1, n - 1). The rat can move in four directions: up(U), down(D), left(L), and right(R).

# 1 represents an open cell through which the rat can move.
# 0 represents a blocked cell that cannot be traversed.
# The rat can move only through open cells and cannot visit the same cell more than once in a path. Return all valid paths as strings consisting of 'U', 'D', 'L', and 'R', representing the sequence of moves taken by the rat.

# Note: Return the paths in lexicographically increasing order. If no valid path exists, return an empty list.


class Solution:
    def ratInMaze(self, maze):
        # code here
        paths = []
        path = ""
        self.find_paths(maze, paths, path, 0, 0)
        return sorted(paths)

    def find_paths(self, maze, paths, path, r, c):

        if r == len(maze) - 1 and c == len(maze[0]) - 1:
            paths.append(path)
            return

        if maze[r][c] == 0:
            return

        maze[r][c] = 2
        if r > 0 and maze[r - 1][c] == 1:
            self.find_paths(maze, paths, path + "U", r - 1, c)
        if r < len(maze) - 1 and maze[r + 1][c] == 1:
            self.find_paths(maze, paths, path + "D", r + 1, c)
        if c > 0 and maze[r][c - 1] == 1:
            self.find_paths(maze, paths, path + "L", r, c - 1)
        if c < len(maze[0]) - 1 and maze[r][c + 1] == 1:
            self.find_paths(maze, paths, path + "R", r, c + 1)
        maze[r][c] = 1
