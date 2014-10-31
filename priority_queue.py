#!/usr/bin/env python
from mineap import Min_Heap

class PriorityQ(object):
    def __init__(self):
        self._heap = Min_Heap()
        self._vals = {}

    #def insert(self, item, priority):
        #self._vals[priority] = item
        #self._heap.push(priority)

    #def pop(self):
        #return self._vals[self._heap.pop()]