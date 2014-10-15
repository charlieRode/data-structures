#!/usr/bin/env python

from linked_list import Linked_List

class Queue:

    def __init__(self):
        self._lst= Linked_List()

    def enqueue(self, datum):
        self._lst.insert(datum)

    def dequeue(self):
        if self._lst.size() > 1:
            trace= self._lst.head
            while trace.pointer.pointer is not None:
                trace= trace.pointer
            result= trace.pointer.datum
            trace.pointer= None
            return result
        elif self._lst.size()==1:
            result= self._lst.head.datum
            self._lst.head= None
            return result
        else:
            raise ValueError("Cannot dequeue an empty queue")

    def size(self):
        return self._lst.size()
