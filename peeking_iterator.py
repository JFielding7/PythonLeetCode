class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.curr = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.curr

    def next(self):
        item = self.curr
        self.curr = self.iter.next() if self.iter.hasNext() else None
        return item

    def hasNext(self):
        return self.curr is not None
