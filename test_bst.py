#!/usr/bin/env python

from bst import BST

def test_init():
    tree = BST()
    assert tree.head == None
