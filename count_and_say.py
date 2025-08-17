import re


class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"

        s = self.countAndSay(n-1)
        res = []

        for digits in map(lambda m: m.group(), re.finditer(r"(\d)\1*", s)):
            res.append(f"{len(digits)}{digits[0]}")

        return "".join(res)


for i in range(1, 20):
    print(Solution().countAndSay(i))
