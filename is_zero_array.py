from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        query_counts = [0] * (len(nums) + 1)

        for query in queries:
            query_counts[query[0]] += 1
            query_counts[query[1] + 1] -= 1

        total_count = 0
        for num, count in zip(nums, query_counts):
            total_count += count
            if num > total_count:
                return False

        return True

