from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        start = 0
        end = len(matrix) * cols - 1

        while start <= end:
            mid = start + end >> 1
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            if num < target:
                start = mid + 1
            else:
                end = mid - 1

        return False