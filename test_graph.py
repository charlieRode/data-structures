#!/usr/bin/env python
import pytest
from graph1 import Edge, Graph


def test_init():
    g = Graph()
    assert len(g._edges) == 0
    assert len(g._nodes) == 0


def test_add_vertex():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    assert 1 in g.nodes()
    assert 2 in g.nodes()


def test_add_edge():
    g = Graph()
    g.add_node(1)
    g.add_edge(3, 2)
    assert len(g.nodes()) == 3
    assert {3, 2} in g.edges()


def test_delete_node():
    g = Graph()
    for n in (1, 2, 3, 4, 5):
        g.add_node(n)