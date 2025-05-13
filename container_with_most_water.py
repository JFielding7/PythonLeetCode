from typing import List
from bisect import bisect_left


def direction_max_area(heights_iter):
    prev_heights = [(next(heights_iter), 0)]
    max_area = 0

    for i, height in enumerate(heights_iter, 1):
        j = bisect_left(prev_heights, height, key=lambda curr_height: curr_height[0])
        if j != len(prev_heights):
            _, k = prev_heights[j]
            max_area = max(max_area, height * (i - k))
        if height > prev_heights[-1][0]:
            prev_heights.append((height, i))

    return max_area

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return max(direction_max_area(iter(heights)), direction_max_area(reversed(heights)))



height = [1,8,6,2,5,4,8,3,7]
res = Solution().maxArea(height)
print(res)
