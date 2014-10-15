#!/usr/bin/env python

"""Tests proper_parenthetics function defined in proper_parenthetics.py
   Can be run with py.test"""

import pytest

from proper_parenthetics import proper_parenthetics

def test_proper_parenthetics():
    s1= "(Happy)"
    s2= ")Sad("
    s3= "fo((o(bar)"
    s4= "()())(())())(((("

    assert proper_parenthetics(s1)== 0
    assert proper_parenthetics(s2)== -1
    assert proper_parenthetics(s3)== 1
    assert proper_parenthetics(s4)== -1