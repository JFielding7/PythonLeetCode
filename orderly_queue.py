class Solution:
    def optimal_rotation(self, s: str):
        length = len(s)
        min_i = 0
        curr_i = 1

        while curr_i < length:
            if s[curr_i] != s[min_i]:
                if s[curr_i] < s[min_i]:
                    min_i = curr_i
                curr_i += 1
                continue

            i = min_i
            j = curr_i

            while i < curr_i:
                i += 1
                j = (j + 1) % len(s)

                if s[j] < s[min_i]:
                    min_i = j
                    j += 1
                    break
                elif s[j] < s[i]:
                    min_i = curr_i
                    break
                elif s[j] > s[i] or s[j] == s[min_i]:
                    break

            if j < curr_i:
                break
            curr_i = j + (s[j] != s[min_i])

        return s[min_i:] + s[:min_i]

    def orderlyQueue(self, s: str, k: int) -> str:
        return "".join(sorted(s)) if k > 1 else self.optimal_rotation(s)

s = "pyplrzxucp"
k = 1
res = Solution().orderlyQueue(s, k)
print(res)
