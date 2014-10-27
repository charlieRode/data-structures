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

    def contains(self, data):
        find = self._search(data)
        if find[0] is None:
            return False
        return True

    def size(self):
        size = {'value': 0}

        def traverse(root):
            if root is not None:
                size['value'] += 1
                traverse(root.lchild)
                traverse(root.rchild)

        traverse(self.root)
        return size['value']

    def depth(self):
        max_depth = {'value': 0}
        depth = {'value': 0}

        def traverse(root):
            if root is not None:
                depth['value'] += 1
                traverse(root.lchild)
                traverse(root.rchild)
                if depth['value'] > max_depth['value']:
                    max_depth['value'] = depth['value']
                depth['value'] -= 1

        traverse(self.root)
        return max_depth['value']

    def balance(self):
        """
        I don't think this is what is being asked for, but
        it does seem to be the literal intepretation of the
        assignment.
        """
        if self.root is None:
            return 0
        l_subtree = BST()
        l_subtree.root = self.root.lchild
        r_subtree = BST()
        r_subtree.root = self.root.rchild
        l_depth = l_subtree.depth()
        r_depth = r_subtree.depth()
        return l_depth - r_depth
