#!/usr/bin/env python

"""Tests Linked_List objects defined in linked_list.py
   Can be run with py.test"""

import pytest

from doublinked import Double_Linked

def test_init():
    dl = Double_Linked()
    assert dl.head is None

def test_insert():
    dl = Double_Linked()
    dl.insert(0)
    dl.insert(1)

    assert dl.head.data == 1
    assert dl.head.last.data == 0
    assert dl.head.last.next.data == 1

def test_append():
    dl = Double_Linked()
    dl.insert(0)
    dl.insert(1)
    dl.append(-1)
    dl.append(-2)

    assert dl.head.data == 1
    assert dl.head.last.last.last.data == -2
    assert dl.head.last.last.last.next.data == -1

def test_pop():
    dl = Double_Linked()
    dl.insert(0)
    dl.insert(1)

    assert dl.pop() == 1
    assert dl.head.data == 0
    assert dl.pop() == 0

def test_shift():
    dl = Double_Linked()
    dl.insert(0)
    dl.insert(1)
    dl.insert(2)

    assert dl.shift() == 0
    assert dl.shift() == 1
    assert dl.shift() == 2

def test_remove():
    lst= Double_Linked()
    lst.insert(7)
    lst.insert(4)
    lst.insert('Sir Sean Connery')
    lst.insert((1, 2, 3))
    lst.remove(4)
    lst.remove('Sir Sean Connery')

    assert lst.size()==2
    assert str(lst)=="((1, 2, 3), 7)"
    lst.remove((1, 2, 3))


