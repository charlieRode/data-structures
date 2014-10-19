#!/usr/bin/env python

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.last = None

class Double_Linked(object):

    def __init__(self):
        self.head = None

    def insert(self, data):
        self.head, self.head.last = Node(data), self.head
        try:
            self.head.last.next = self.head
        except AttributeError:
            pass

    def append(self, data):
        trace = self.head
        while trace.last is not None:
            trace = trace.last
        trace.last, trace.last.next = Node(data), trace

    def pop(self):
        popped = self.head.data
        self.head = self.head.last
        return popped

    def shift(self):
        trace = self.head
        while trace.last is not None:
            trace = trace.last
        try:
            trace.next.last = None
        except AttributeError:
            self.head = None
        return trace.data

    def remove(self, item):
        if self.head.data == item:
            self.head = self.head.last
        else:
            try:
                trace = self.head
                while trace.last.data != item:
                    trace = trace.last
                trace.last = trace.last.last
            except AttributeError:
                raise ValueError("%s not in list" % str(item))

    def size(self):
        """Will count the number of non-None elements in the linked list"""
        trace = self.head
        count = 0
        while trace is not None:
            trace = trace.last
            count += 1
        return count

    def __str__(self):
        result = ()
        trace = self.head
        while trace is not None:
            result += (trace.data,)
            trace = trace.last

        return str(result)
