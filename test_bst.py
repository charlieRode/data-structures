#!/usr/bin/env python

from bst import BST, Node

def test_init():
    tree = BST()
    assert tree.root == None

def test_insert():
    tree = BST()
    tree.insert(0)
    tree.insert(-2)
    tree.insert(2)
    tree.insert(-1)
    tree.insert(3)
    tree.insert(-3)
    tree.insert(3)
    tree.insert(1)

    assert tree.root.data == 0
    assert tree.root.lchild.data == -2
    assert tree.root.lchild.lchild.data == -3
    assert tree.root.lchild.rchild.data == -1
    assert tree.root.rchild.data == 2
    assert tree.root.rchild.rchild.data == 3
    assert tree.root.rchild.lchild.data == 1

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
    tree = BST()
    tree.insert(0)
    tree.insert(1)
    tree.insert(-1)
    tree.insert(2)
    tree.insert(-2)
    assert tree.contains(-1) == True
    assert tree.contains(0) == True
    assert tree.contains(4) == False

def test_size():
    tree = BST()
    assert tree.size() == 0
    tree.insert(0)
    assert tree.size() == 1
    tree.insert(2)
    tree.insert(1)
    assert tree.size() == 3
    tree.insert(-1)
    tree.insert(-2)
    tree.insert(4)
    assert tree.size() == 6