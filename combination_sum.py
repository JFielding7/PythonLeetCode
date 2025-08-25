def get_possible_sums(candidates: List[int], target: int) -> List[List[bool]]:
    possible_sums = [[True] + [False] * target for _ in range(len(candidates))]

    for i, num in enumerate(candidates):
        for total in range(1, target + 1):
            possible_sums[i][total] = (i > 0 and possible_sums[i - 1][total]) or (
                        num <= total and possible_sums[i][total - num])

    return possible_sums


def get_combos(candidates, end, target, possible_sums, curr_combo, combos):
    if end < 0 or not possible_sums[end][target]:
        return

    i = 0
    curr_num = candidates[end]

    while target > 0:
        i += 1
        get_combos(candidates, end - 1, target, possible_sums, curr_combo, combos)
        target -= curr_num
        curr_combo.append(curr_num)

    if target == 0:
        combos.append(curr_combo[:])

    for _ in range(i):
        curr_combo.pop()


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        possible_sums = get_possible_sums(candidates, target)
        get_combos(candidates, len(candidates) - 1, target, possible_sums, [], combos)
        return combos
