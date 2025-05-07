from typing import List


class Heap:
    def __init__(self):
        self.arr = []
        self.indices = {}

    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]
        self.indices[self[i][1]] = i
        self.indices[self[j][1]] = j

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) >> 1
            if self[i] < self[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def heapify_down(self, i):
        curr_len = len(self)
        max_index = (curr_len - 1) >> 1

        while i < max_index:
            min_child_i = (i << 1) + 1
            if self[min_child_i + 1] < self[min_child_i]:
                min_child_i += 1
            if self[min_child_i] < self[i]:
                self.swap(i, min_child_i)
                i = min_child_i
            else:
                break

        if (curr_len & 1) == 0 and i == max_index and self[i]  > self[(i << 1) + 1]:
            self.swap(i, (i << 1) + 1)

    def push(self, num, i):
        j = self.indices.get(i)
        if j is None:
            curr_len = len(self)
            self.arr.append((num, i))
            self.indices[i] = curr_len
            self.heapify_up(curr_len)
        else:
            self[j] = (num, i)
            self.heapify_down(j)

    def others_min(self, i):
        num, j = self[0]
        return num if i != j else min(self[1][0], self[2][0] if len(self) > 2 else float('inf'))

    def __getitem__(self, i):
        return self.arr[i]

    def __setitem__(self, i, value):
        self.arr[i] = value

    def __len__(self):
        return len(self.arr)


class Solution:
    def sorted_nums(self, nums):
        arr = []

        for i, lst in enumerate(nums):
            for num in lst:
                arr.append((num, i))

        arr.sort()
        return arr

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        list_count = len(nums)
        if list_count == 1:
            return [nums[0][0], nums[0][0]]

        lower = upper = None
        heap = Heap()

        for num, i in self.sorted_nums(nums):
            heap.push(num, i)
            if len(heap) == list_count:
                max_lower = heap.others_min(i)
                if lower is None or num - max_lower < upper - lower:
                    lower = max_lower
                    upper = num

        return [lower, upper]





s = Solution()
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print(s.smallestRange(nums))

