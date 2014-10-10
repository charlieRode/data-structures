#!/usr/bin/env python

from linked_list import Linked_List

class Stack:

    def __init__(self):
        self._lst= Linked_List()

    def push(self, datum):
        self._lst.insert(datum)

    def pop(self):
        return self._lst.pop()