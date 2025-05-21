from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row = matrix[0]
        zero_marker = 1 if 0 in first_row else 0
        rows = len(matrix)
        cols = len(first_row)

        for i, row in enumerate(matrix):
            if 0 in row:
                for j in range(cols):
                    if row[j] == 0:
                        first_row[j] = zero_marker
                    else:
                        row[j] = 0

        for j, num in enumerate(first_row):
            if num == zero_marker:
                for i in range(rows):
                    matrix[i][j] = 0






