class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        period = (numRows-1) << 1
        zigzag = [s[::period]]
        length = len(s)

        for row in range(1, numRows - 1):
            step = period - (row << 1)
            i = row

            while i < length:
                zigzag.append(s[i])
                i += step
                step = period - step

        zigzag.append(s[numRows-1::period])
        return "".join(zigzag)


s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))