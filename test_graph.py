#!/usr/bin/env python
import pytest
from graph import Edge, Graph


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
    try:
        g.delete_node('a')
    except IndexError:
        assert True
    else:
        assert False
    for letter in ['a', 'b', 'c', 'd']:
        g.add_node(letter)
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.delete_node('d')
    for edge in g._edges:
        assert 'd' not in edge.connects
    assert len(g._edges) == 3
    g.delete_node('a')
    assert len(g._edges) == 1
    for edge in g._edges:
        assert edge.connects == {'b', 'c'}
