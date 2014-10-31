#!/usr/bin/env python
from minheap import Min_Heap


class PriorityQ(object):
    def __init__(self):
        self._heap = Min_Heap()
        self._vals = {}

    def insert(self, item, priority):
        """Given an item and a priority, in that order, adds item to Q"""
        if type(priority) is not int:
            raise TypeError("priority must be type int")
        else:
            if priority in self._vals.keys():
                self._vals[priority] += (item,)
            else:
                self._vals[priority] = (item,)
                self._heap.push(priority)

    def pop(self):
        try:
            popped = self._vals[self._heap.pop()][0]
        except IndexError:
            raise IndexError("can't pop from empty priority queue")
        return popped

    def peek(self):
        try:
            seen = self._vals[self._heap._lst[1]][0]
        except IndexError:
            raise IndexError("priority queue is empty")
        return seen
