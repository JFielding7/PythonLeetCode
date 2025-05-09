from typing import List
from itertools import islice

class Heap:
    def __init__(self, arr, is_max=False):
        self.arr = arr
        self.indices = {pair[1]: i for i, pair in enumerate(arr)}
        self.cmp = int.__lt__
        self.cmp_or_eq = int.__le__
        if is_max:
            self.cmp = int.__gt__
            self.cmp_or_eq = int.__ge__


    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]
        self.indices[self[i][1]] = i
        self.indices[self[j][1]] = j

    def cmp_vals(self, i, j):
        return self.cmp(self.arr[i][0], self.arr[j][0])

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) >> 1
            if self.cmp_vals(i, parent):
                self.swap(i, parent)
                i = parent
            else:
                break

    def heapify_down(self, i):
        curr_len = len(self)
        max_index = (curr_len - 1) >> 1

        while i < max_index:
            min_child_i = (i << 1) + 1
            if self.cmp_vals(min_child_i + 1, min_child_i):
                min_child_i += 1
            if self.cmp_vals(min_child_i, i):
                self.swap(min_child_i, i)
                i = min_child_i
            else:
                break

        if (curr_len & 1) == 0 and i == max_index and self.cmp_vals((i << 1) + 1, i):
            self.swap((i << 1) + 1, i)

    def insert(self, num, key, i=None) -> None:
        if i is None:
            i = len(self)
        self.indices[key] = i
        self.arr.append((num, key))
        self.heapify_up(i)

    def remove(self, i):
        prev_num, prev_key = self[i]
        del self.indices[prev_key]
        if i == len(self) - 1:
            self.arr.pop()
        else:
            last_num, last_key = last = self.arr.pop()
            self[i] = last
            self.indices[last_key] = i
            if self.cmp(last_num, prev_num):
                self.heapify_up(i)
            else:
                self.heapify_down(i)

    def get_index(self, key):
        return self.indices.get(key)

    def update_index(self, i, num, key):
        prev_num, prev_key = self[i]
        del self.indices[prev_key]
        self[i] = (num, key)
        self.indices[key] = i
        if self.cmp(num, prev_num):
            self.heapify_up(i)
        else:
            self.heapify_down(i)

    def __getitem__(self, i):
        return self.arr[i]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __len__(self):
        return len(self.arr)


class Solution:
    def update_heaps(self, num, key, heap_to_rm_from, rm_i, other_heap):
        if len(other_heap) > 0 and other_heap.cmp_or_eq(num, other_heap[0][0]):
            heap_to_rm_from.update_index(rm_i, num, key)
        else:
            if len(heap_to_rm_from) > len(other_heap):
                heap_to_rm_from.remove(rm_i)
                other_heap.insert(num, key)
            else:
                other_root = other_heap[0]
                heap_to_rm_from.update_index(rm_i, other_root[0], other_root[1])
                other_heap.update_index(0, num, key)

    def update_window(self, rm_key, add_key, num, lower_heap, upper_heap) -> None:
        lower_idx = lower_heap.get_index(rm_key)

        if lower_idx is not None:
            self.update_heaps(num, add_key, lower_heap, lower_idx, upper_heap)
        else:
            self.update_heaps(num, add_key, upper_heap, upper_heap.get_index(rm_key), lower_heap)

    def get_median(self, lower_heap, upper_heap):
        lower_len = len(lower_heap)
        upper_len = len(upper_heap)
        print(upper_len, lower_len)

        if lower_len == upper_len:
            return (lower_heap[0][0] + upper_heap[0][0]) / 2

        return lower_heap[0][0] if lower_len > upper_len else upper_heap[0][0]

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(map(lambda pair: (pair[1], pair[0]), enumerate(islice(nums, k))))
        medians = [(window[(k - 1) >> 1][0] + window[k >> 1][0]) / 2]

        lower_heap = Heap(window[(k-1)>>1::-1], is_max=True)
        upper_heap = Heap(window[((k-1)>>1)+1:])
        print(lower_heap.arr, " ", upper_heap.arr)

        for i in range(len(nums) - k):
            self.update_window(i, i + k, nums[i + k], lower_heap, upper_heap)
            medians.append(self.get_median(lower_heap, upper_heap))
            print(lower_heap.arr, " ", upper_heap.arr)
        return medians


x = Solution()
nums = [1,2]
k = 1
res = x.medianSlidingWindow(nums, k)
print(res)

