from typing import List


def next_interval(interval_iter):
    return next(interval_iter, (-1, -1))

class Solution:
    def intervalIntersection(self, list0: List[List[int]], list1: List[List[int]]) -> List[List[int]]:
        intersection = []
        intervals0 = map(tuple, list0)
        intervals1 = map(tuple, list1)
        start0, end0 = next_interval(intervals0)
        start1, end1 = next_interval(intervals1)

        while start0 >= 0 and start1 >= 0:
            if start1 <= start0 <= end1:
                intersection.append([start0, min(end0, end1)])
            elif start0 <= start1 <= end0:
                intersection.append([start1, min(end0, end1)])
            if end0 < end1:
                start0, end0 = next_interval(intervals0)
            else:
                start1, end1 = next_interval(intervals1)

        return intersection
