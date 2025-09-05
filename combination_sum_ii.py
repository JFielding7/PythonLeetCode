from collections import Counter

def combos(nums, start, length, curr_combo, target, total_combos):
    curr_num, curr_count = nums[start]
    max_count = min(curr_count, target // curr_num)

    if start < length - 1:
        combos(nums, start + 1, length, curr_combo, target, total_combos)

        for _ in range(max_count):
            target -= curr_num
            curr_combo.append(curr_num)
            if target == 0:
                total_combos.append(curr_combo[:])
                break
            combos(nums, start + 1, length, curr_combo, target, total_combos)

        for _ in range(max_count):
            curr_combo.pop()
    elif target - curr_num * max_count == 0:
        total_combos.append(curr_combo + [curr_num] * max_count)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        total_combos = []
        nums = [*Counter(candidates).items()]
        combos(nums, 0, len(nums), [], target, total_combos)
        return total_combos
