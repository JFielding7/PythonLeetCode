from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        upper_amount = amount + 1
        combos = [0] * upper_amount
        combos[0] = 1

        for coin in coins:
            for curr_amount in range(coin, upper_amount):
                combos[curr_amount] += combos[curr_amount - coin]

        return combos[-1]



a = 5
c = [1,2,5]

print(Solution().change(a, c))