#!/usr/bin/env python


class Min_Heap(object):

    def __init__(self, data=[]):
        self._lst = [None]
        for item in data:
            self._lst.insert(1, item)
            self.percolate()

    def push(self, item):
        self._lst.insert(1, item)
        self.percolate()

    def pop(self):
        try:
            popped = self._lst[1]
            if len(self._lst) > 2:
                self._lst[1] = self._lst.pop()
                self.percolate()
            else:
                self._lst = [None]
            return popped
        except IndexError:
            raise IndexError("can't pop from an empty heap")

    def percolate(self):
        x = self._lst[1]
        while True:
            try:
                i = self._lst.index(x)
                j = 2*i if self._lst[2*i] <= self._lst[2*i + 1] else 2*i + 1
                if x > self._lst[j]:
                    self._lst[i], self._lst[j] = self._lst[j], self._lst[i]
                else:
                    break
            except IndexError:
                break
