#!/usr/bin/env python

"""Tests Stack objects defined in stack.py
   Can be run with py.test"""

from queue import Queue

def test_init():
    q= Queue()
    assert q._lst.head==None

def test_enqueue():
    q= Queue()
    
    q.enqueue("Jack")
    assert q._lst.head.datum=="Jack"

    q.enqueue("Jill")
    assert q._lst.head.datum=="Jill"

def test_dequeue():
    q= Queue()

    q.enqueue("Red")
    q.enqueue("Blue")
    q.enqueue("Green")
    q.enqueue("Yellow")

    assert q.dequeue()== "Red"
    assert q.dequeue()== "Blue"
    assert q.dequeue()== "Green"
    assert q.dequeue()== "Yellow"
    try:
        q.dequeue()
        assert False
    except ValueError:
        assert True

def test_size():
    q= Queue()
    for i in range(100):
        q.enqueue(i)

    assert q.size()== 100
    for j in range(50):
        q.dequeue()
    assert q.size()== 50