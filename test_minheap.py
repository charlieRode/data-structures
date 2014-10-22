#!/usr/bin/env python

import pytest
from minheap import Min_Heap

def test_init():
    h = Min_Heap()
    assert h._lst == [None]
    h = Min_Heap((5, 4, 3, 2, 1))
    assert h._lst[1] == 1
    h = Min_Heap([1, 3, 4, 2, 0, 8])
    assert h._lst[1] == 0

def test_push():
    h = Min_Heap()
    h.push(4)
    assert h._lst[1] == 4
    h.push(3)
    assert h._lst[1] == 3
    h.push(5)
    assert h._lst[1] == 3

def test_pop():
    h = Min_Heap((5, 4, 3, 2, 1))
    assert h.pop() == 1
    assert h.pop() == 2
    assert h.pop() == 3
    assert h.pop() == 4
    assert h.pop() == 5
    try:
        h.pop()
        assert False
    except IndexError:
        assert True