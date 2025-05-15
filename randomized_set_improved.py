from collections import defaultdict
from random import Random


class RandomizedCollection:
    def __init__(self):
        self.indices = defaultdict(set)
        self.arr = []
        self.rand_dev = Random()

    def insert(self, val: int) -> bool:
        not_present = val not in self.indices
        self.indices[val].add(len(self.arr))
        self.arr.append(val)
        return not_present

    def remove(self, val: int) -> bool:
        indices = self.indices.get(val)
        if indices is None:
            return False

        index = indices.pop()
        if len(indices) == 0:
            del self.indices[val]

        last_index = len(self.arr) - 1

        if index != last_index:
            last_val = self.arr[last_index]
            self.arr[index] = last_val
            indices = self.indices[last_val]
            indices.remove(last_index)
            indices.add(index)

        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return self.arr[self.rand_dev.randrange(0, len(self.arr))]
