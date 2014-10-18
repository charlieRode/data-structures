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