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

    #def pop(self):
        #return self._vals[self._heap.pop()]