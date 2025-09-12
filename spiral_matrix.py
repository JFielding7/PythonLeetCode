class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_row, max_row, min_col, max_col = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        r, dr, c, dc = 0, 0, 0, 1
        nums = []

        for _ in range((max_row + 1) * (max_col + 1)):
            nums.append(matrix[r][c])

            if dc == 1 and c == max_col:
                min_row += 1
                dr, dc = 1, 0
            elif dr == 1 and r == max_row:
                max_col -= 1
                dr, dc = 0, -1
            elif dc == -1 and c == min_col:
                max_row -= 1
                dr, dc = -1, 0
            elif dr == -1 and r == min_row:
                min_col += 1
                dr, dc = 0, 1

            r += dr
            c += dc

        return nums
