import random
from random import Random


class RandomizedSet:
    def __init__(self):
        self.indices = {}
        self.arr = []
        self.rand_dev = Random()

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        index = self.indices.pop(val, None)
        if index is None:
            return False

        if (len(self.indices) << 1) > len(self.arr):
            self.arr[index] = None
        else:
            indices = {}
            self.arr = []
            for i, num in enumerate(self.indices):
                indices[num] = i
                self.arr.append(num)
            self.indices = indices

        return True

    def getRandom(self) -> int:
        curr_len = len(self.arr)
        i = self.rand_dev.randrange(0, curr_len)

        while self.arr[i] not in self.indices:
            i = self.rand_dev.randrange(0, curr_len)

        return self.arr[i]


print(random.Random().randrange(1, 3))
