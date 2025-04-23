from typing import List


def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    paths = [[1]*cols for _ in matrix]

    cells = []
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            cells.append((num, i, j))
    cells.sort()

    delta = ((0, -1), (0, 1), (-1, 0), (1, 0))
    longest = 1
    for num, i, j in cells:
        max_len = 1
        for dr, dc in delta:
            r = i + dr
            c = j + dc
            if 0 <= r < rows and 0 <= c < cols and num > matrix[r][c] and (curr_len := paths[r][c] + 1) > max_len:
                max_len = curr_len
        paths[i][j] = max_len
        if max_len > longest:
            longest = max_len

    return longest




