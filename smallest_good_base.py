class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        for bits in range(n.bit_length(), 1, -1):
            base = int(n ** (1 / (bits - 1)))
            if n == (base ** bits - 1) // (base - 1):
                return str(base)

        return str(n - 1)
