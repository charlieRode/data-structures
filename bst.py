#!/usr/bin/env python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST(object):
    def __init__(self):
        self.root = None

    def _search(self, data):
        if self.root is None:
            return (None,)
        trace = self.root
        while trace is not None:
            print trace.data
            if trace.data == data:
                return (trace,)
            elif data < trace.data:
                trace, _parent = trace.lchild, trace
            else:
                trace, _parent = trace.rchild, trace
        return (trace, _parent)
  

    def insert(self, data):
        pass
