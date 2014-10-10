#!/usr/bin/env python

"""Tests Linked_List objects defined in linked_list.py
   Can be run with py.test"""

import pytest

from linked_list import Linked_List

def test_init():
    lst= Linked_List()

    assert lst.head is None

def test_insert():
    lst= Linked_List()
    lst.insert(7)

    assert lst.head.datum==7

    lst.insert('Sir Sean Connery')

    assert lst.head.datum=='Sir Sean Connery'

def test_pop():
    lst= Linked_List()
    lst.insert(7)
    lst.insert('Sir Sean Connery')
    val1= lst.pop()
    val2= lst.pop()

    assert val1=='Sir Sean Connery'
    assert val2==7
    assert lst.head is None

def test_size():
    lst= Linked_List()
    lst.insert(0)
    lst.insert(1)
    lst.insert(45)
    lst.insert('turds')

    assert lst.size()==4
    assert lst.head.datum=='turds'
    lst.pop()
    lst.pop()
    assert lst.size()==2
    assert lst.head.datum==1
    lst.insert('boobies')
    assert lst.size()==3
    lst.insert('i am mature')
    assert lst.size()==4
    lst.pop()
    assert lst.head.datum=='boobies'

def test_search():
    lst= Linked_List()
    lst.insert(7)
    lst.insert(4)
    lst.insert('Sir Sean Connery')
    lst.insert((1, 2, 3))
    lst.insert('Harrison Ford')
    n1= lst.search('Sir Sean Connery')
    n2= lst.search(7)

    assert n1.datum=='Sir Sean Connery'
    assert n2.pointer is None
    assert lst.search('Batman') is None

def test_remove():
    lst= Linked_List()
    lst.insert(7)
    lst.insert(4)
    lst.insert('Sir Sean Connery')
    lst.insert((1, 2, 3))
    lst.remove(4)
    lst.remove('Sir Sean Connery')

    assert lst.size()==2
    assert str(lst)=="((1, 2, 3), 7)"
    lst.remove((1, 2, 3))

    assert str(lst)=="(7,)"

def test_print():
    lst= Linked_List()
    lst.insert('A')
    lst.insert((1, 2, 3))
    lst.insert(42)
    lst.insert('Bob Dole')

    assert str(lst) == "('Bob Dole', 42, (1, 2, 3), 'A')"
