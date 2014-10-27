#!/usr/bin/env python

class Node(object):
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BST(object):
    def __init__(self):
        self.head = None
        