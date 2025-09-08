class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = len(nums) - 1
        max_reach = 0

        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
            if max_reach >= max_idx:
                return True
