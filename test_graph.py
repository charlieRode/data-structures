#!/usr/bin/env python
import pytest
from graph import Edge, Graph


def test_init():
    g = Graph()
    assert len(g._edges) == 0
    assert len(g._verticies) == 0


def test_add_vertex():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    assert 1 in g.nodes()
    assert 2 in g.nodes()

def test_add_edge():
    g = Graph()
    g.add_vertex(1)
    g.add_edge(3, 2)
    assert len(g.nodes()) == 3
    assert {3, 2} in g.edges()