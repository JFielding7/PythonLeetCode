from heapq import heappush, heapreplace


class MedianFinder:
    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        lower_len = len(self.lower)
        upper_len = len(self.upper)

        if lower_len == upper_len:
            if lower_len == 0 or num < self.upper[0]:
                heappush(self.lower, -num)
            else:
                heappush(self.upper, num)
        elif lower_len < upper_len:
            if num <= self.upper[0]:
                heappush(self.lower, -num)
            else:
                prev_root = heapreplace(self.upper, num)
                heappush(self.lower, -prev_root)
        else:
            if num >= -self.lower[0]:
                heappush(self.upper, num)
            else:
                prev_root = -heapreplace(self.lower, -num)
                heappush(self.upper, prev_root)


    def findMedian(self) -> float:
        lower_len = len(self.lower)
        upper_len = len(self.upper)

        if lower_len == upper_len:
            return (self.upper[0] - self.lower[0]) / 2

        return self.upper[0] if lower_len < upper_len else -self.lower[0]
