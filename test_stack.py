#!/usr/bin/env python

"""Tests Stack objects defined in stack.py
   Can be run with py.test"""

import pytest

from stack import Stack

def test_init():
    stack= Stack()

    assert stack._lst.head is None

def test_push():
    stack= Stack()
    
    stack.push(0)
    assert stack._lst.head.datum==0

    stack.push('dookie')
    assert stack._lst.head.datum=='dookie'

def test_pop():
    stack= Stack()

    stack.push('a')
    stack.push('b')

    p= stack.pop()

    assert p== 'b'
    assert stack._lst.head.datum== 'a'