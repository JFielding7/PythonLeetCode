from heapq import heapify
from typing import List


class Solution:
    def nums_heap(self, nums):
        heap = []

        for i, lst in enumerate(nums):
            for num in lst:
                heap.append((num, i))

        heapify(heap)
        return heap

    def other_lists_min(self, heap, i):


    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        lower = upper = None
        min_diff = float('inf')
        heap = self.nums_heap(nums)

        for num, i in heap:





s = Solution()
print(s.smallestRange([[1]]))

