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


def test_pop():
    p = PriorityQ()
    p.insert('item1', 1)
    p.insert('item2', 2)
    p.insert('item3', 0)

    assert p.pop() == 'item3'
    assert p.pop() == 'item1'
    assert p.pop() == 'item2'
    try:
        p.pop()
        assert False
    except IndexError:
        assert True


def test_peek():
    p = PriorityQ()
    p.insert('jack', 1)
    p.insert('jill', 2)
    p.insert('steve', 0)

    assert p.peek() == 'steve'
    p.pop()
    assert p.peek() == 'jack'
