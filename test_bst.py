#!/usr/bin/env python

from bst import BST, Node

def test_init():
    tree = BST()
    assert tree.root == None

def test_insert():
    return
    tree = BST()
    tree.insert(0)
    assert tree.root.data == 0
    tree.insert(1)
    assert tree.root.data == 1
    assert tree.root.lchild == None
    assert tree.root.rchild.data == 1
    tree.insert(-1)
    assert tree.root.lchild.data == -1

def test_search():
    tree = BST()
    assert tree._search(0)[0] is None

    tree.root = Node(0)
    tree.root.lchild = Node(-2)
    tree.root.rchild = Node(2)
    tree.root.lchild.lchild = Node(-3)
    tree.root.lchild.rchild = Node(-1)
    tree.root.rchild.rchild = Node(3)
    tree.root.rchild.lchild = Node(1)

    assert tree._search(1)[0].data == 1
    assert tree._search(-2)[0].data == -2
    assert tree._search(4)[0] is None
    assert tree._search(4)[1].data == 3


def test_contains():
    return
    tree = BST()
    tree.insert(0)
    tree.insert(1)
    tree.insert(-1)
    tree.insert(2)
    tree.insert(-2)
    assert tree.contains(-1) == True
    assert tree.contains(0) == True
    assert tree.contains(4) == False
