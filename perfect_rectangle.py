from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        max_x = float('-inf')
        min_x = float('inf')
        max_y = float('-inf')
        min_y = float('inf')
        total_area = 0

        for x0, y0, x1, y1 in rectangles:
            min_x = min(min_x, x0)
            max_x = max(max_x, x1)
            min_y = min(min_y, y0)
            max_y = max(max_y, y1)
            total_area += (x1 - x0) * (y1 - y0)

        if total_area != (max_x - min_x) * (max_y - min_y):
            return False

        lines_up = {min_y: (min_x, max_y)}
        lines_down = {max_y: (min_x, min_y)}
        rectangles.sort()

        for x0, y0, x1, y1 in rectangles:
            # print(lines_up)
            # print(lines_down)
            # print(x0, y0, x1, y1)
            # print()
            line = lines_up.get(y0)
            if line is None:
                return False

            x, prev_end_y = line
            if x0 != x or y1 > prev_end_y:
                return False

            next_start_y = y0
            next_end_y = y1

            if y1 == prev_end_y:
                line_above = lines_up.get(y1)
                if line_above is not None:
                    x2, y2 = line_above
                    if x1 == x2:
                        next_end_y = y2
                        del lines_up[y1]
            else:
                lines_up[y1] = (x, prev_end_y)
                lines_down[prev_end_y] = (x, y1)

            line_below = lines_down.get(y0)
            if line_below is not None:
                x2, y2 = line_below
                if x1 == x2:
                    next_start_y = y2
                    del lines_down[y0]

            lines_up[next_start_y] = (x1, next_end_y)
            lines_down[next_end_y] = (x1, next_start_y)

        return True


rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
print(Solution().isRectangleCover(rectangles))