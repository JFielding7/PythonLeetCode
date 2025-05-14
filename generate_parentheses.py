from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combos = [[""], ["()"]]

        for i in range(2, n+1):
            curr_combos = []

            for j in range(i):
                for combo0 in combos[j]:
                    for combo1 in combos[i - j - 1]:
                        curr_combos.append(f"({combo0}){combo1}")

            combos.append(curr_combos)

        return combos[-1]
