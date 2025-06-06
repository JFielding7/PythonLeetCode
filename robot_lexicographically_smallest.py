class Solution:
    def robotWithString(self, s: str) -> str:
        length = len(s)
        min_char = 'z'
        mins = [0] * length

        for i, char in enumerate(reversed(s)):
            min_char = min(min_char, char)
            mins[length - i - 1] = min_char

        paper = []
        stack = []
        i = 0

        while i < length:
            if s[i] == mins[i]:
                paper.append(s[i])
                i += 1
                while stack and (i == length or stack[-1] <= mins[i]):
                    paper.append(stack.pop())
            else:
                stack.append(s[i])
                i += 1

        return ''.join(paper)


print(Solution().robotWithString('bydizfve'))
