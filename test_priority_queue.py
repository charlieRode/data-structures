#!/usr/bin/env python
import pytest
from priority_queue import PriorityQ

def test_init():
    p = PriorityQ()
    assert len(p._vals) == 0
