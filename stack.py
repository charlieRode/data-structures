#!/usr/bin/env python

from linked_list import Linked_List
lst= Linked_List()

class Stack:

    def __init__(self):
        self.top= lst.head

    def push(self, datum):
        lst.insert(datum)
        self.top= lst.head.datum

    def pop(self):
        result= lst.pop()
        self.top= lst.head.datum
        return result
