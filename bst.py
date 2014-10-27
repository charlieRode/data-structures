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
        _parent = None
        if self.root is None:
            return (None,)
        trace = self.root
        while trace is not None:
            if trace.data == data:
                return (trace, _parent)
            elif data < trace.data:
                trace, _parent = trace.lchild, trace
            else:
                trace, _parent = trace.rchild, trace
        return (trace, _parent)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        try:
            if self._search(data)[0].data == data:
                return
        except AttributeError:
            _parent = self._search(data)[1]
            if data < _parent.data:
                _parent.lchild = Node(data)
            else:
                _parent.rchild = Node(data)
        return
