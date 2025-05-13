from typing import List
from bisect import bisect_right
from collections import defaultdict


def max_score(boxes, indices, additional_boxes, start, end, cache):
    if start > end:
        return 0
    if start == end:
        return (additional_boxes + boxes[start][1]) ** 2

    score = cache.get((additional_boxes, start, end))
    if score is not None:
        return score

    num, box_count = boxes[start]
    new_additional_boxes = additional_boxes + box_count
    score = new_additional_boxes ** 2 + max_score(boxes, indices, 0, start + 1, end, cache)
    curr_indices = indices[num]

    for i in range(bisect_right(curr_indices, start), len(curr_indices)):
        index = curr_indices[i]
        if index > end:
            break
        score = max(score,
                    max_score(boxes, indices, 0, start + 1, index - 1, cache) +
                    max_score(boxes, indices, new_additional_boxes, index, end, cache))

    cache[(additional_boxes, start, end)] = score
    return score

def combine(boxes):
    combined = []
    indices = defaultdict(list)
    prev = boxes[0]
    count = 1

    for i in range(1, len(boxes)):
        curr = boxes[i]
        if prev == curr:
            count += 1
        else:
            indices[prev].append(len(combined))
            combined.append((prev, count))
            count = 1
            prev = curr
    indices[prev].append(len(combined))
    combined.append((prev, count))

    return combined, indices


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        combined_boxes, indices = combine(boxes)
        return max_score(combined_boxes, indices, 0, 0, len(combined_boxes) - 1, {})


# r = [1, 2, 2, 4, 5]
# print(bisect_right(r, 3))
boxes = [1,3,2,2,2,3,4,3,1]
res = Solution().removeBoxes(boxes)
print(res)
