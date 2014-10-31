#!/usr/bin/env python
import pytest
from priority_queue import PriorityQ

def test_init():
    p = PriorityQ()
    assert len(p._vals) == 0

def test_insert():
    p = PriorityQ()
    p.insert("Tom Jones", 2)
    p.insert(5, 1)
    p.insert('X', 1)

    try:
        p.insert('stuff', 'a_string')
    except TypeError:
        assert True
    else:
        assert False

    assert "Tom Jones" in p._vals[2]
    assert 5 in p._vals[1]
    assert 'X' in p._vals[1]