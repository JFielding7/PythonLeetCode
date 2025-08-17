MOD = 1000000007


class Solution:
    def countOrders(self, n: int) -> int:
        res = 1

        for i in range(2, n + 1):
            res = ((2 * i * i - i) * res) % MOD

        return res
