#!/usr/bin/env python
import pytest
from graph import Edge, Vertext, Graph


def test_init():
    g = Graph()
    assert g.edges == []
    assert g.verticies == []