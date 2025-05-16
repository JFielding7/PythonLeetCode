from typing import List


class Solution:
    def minSwap(self, nums0: List[int], nums1: List[int]) -> int:
        length = len(nums0)
        prev_no_swap = 0
        prev_swap = 1

        for i in range(1, length):
            print(prev_no_swap, prev_swap)
            curr_no_swap = curr_swap = length
            if nums0[i] > nums0[i - 1] and nums1[i] > nums1[i - 1]:
                curr_no_swap = min(curr_no_swap, prev_no_swap)
                curr_swap = min(curr_swap, prev_swap + 1)
            if nums0[i] > nums1[i - 1] and nums1[i] > nums0[i - 1]:
                curr_no_swap = min(curr_no_swap, prev_swap)
                curr_swap = min(curr_swap, prev_no_swap + 1)

            prev_no_swap = curr_no_swap
            prev_swap = curr_swap

        return min(prev_no_swap, prev_swap)


nums0 = [1,3,5,4]
nums1 = [1,2,3,7]

print(Solution().minSwap(nums0, nums1))