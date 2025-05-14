from typing import List


def distance(a, b):
    return

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        remaining = {(point[0], point[1]): float('inf') for point in points}
        cost = 0
        first = points[0]
        curr_point = (first[0], first[1])

        while len(remaining) > 1:
            del remaining[curr_point]
            min_dist = float('inf')
            min_point = None

            for point in remaining:
                dist = min(remaining[point], abs(curr_point[0]-point[0]) + abs(curr_point[1]-point[1]))
                if dist < min_dist:
                    min_dist = dist
                    min_point = point
                remaining[point] = dist

            cost += min_dist
            curr_point = min_point

        return cost


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))


