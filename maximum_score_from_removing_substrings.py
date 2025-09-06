class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            greater_start, less_start = 'a', 'b'
            greater_gain, less_gain = x, y
        else:
            greater_start, less_start = 'b', 'a'
            greater_gain, less_gain = y, x

        gain = 0
        greater_start_count = 0
        less_start_count = 0

        for c in s:
            if c == greater_start:
                greater_start_count += 1
            elif c == less_start:
                if greater_start_count:
                    greater_start_count -= 1
                    gain += greater_gain
                else:
                    less_start_count += 1
            else:
                gain += less_gain * min(less_start_count, greater_start_count)
                greater_start_count = less_start_count = 0

        return gain + less_gain * min(less_start_count, greater_start_count)
